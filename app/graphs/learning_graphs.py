from __future__ import annotations

from app.agents.research_team import research_agent, reviewer_agent, writer_agent
from app.state.schemas import AgentState, ResearchState
from app.tools.basic_tools import equation_solver_tool, source_triage_tool, text_analyzer_tool

try:
    from langgraph.graph import END, START, StateGraph
except ModuleNotFoundError:
    END = "__end__"
    START = "__start__"
    StateGraph = None


def hello_node(state: AgentState) -> AgentState:
    name = state.get("user_message", "student")
    return {"response": f"Hello, {name}. Welcome to LangGraph."}


def joke_node(state: AgentState) -> AgentState:
    return {"response": "A graph node walked into a bar and found the shortest path."}


def fact_node(state: AgentState) -> AgentState:
    return {"response": "Fact: LangGraph represents workflows as stateful graphs."}


def tool_node(state: AgentState) -> AgentState:
    message = state.get("user_message", "")
    return tool_selection_graph(message)


def route_message(message: str) -> str:
    lowered = message.lower()
    if "joke" in lowered:
        return "joke"
    if any(term in lowered for term in ("equation", "solve", "analyze", "text", "source", "triage")):
        return "tool"
    return "fact"


def route_state(state: AgentState) -> str:
    return route_message(state.get("user_message", ""))


def build_hello_graph():
    if StateGraph is None:
        return None
    graph = StateGraph(AgentState)
    graph.add_node("hello", hello_node)
    graph.add_edge(START, "hello")
    graph.add_edge("hello", END)
    return graph.compile()


def build_conditional_graph():
    if StateGraph is None:
        return None
    graph = StateGraph(AgentState)
    graph.add_node("joke", joke_node)
    graph.add_node("fact", fact_node)
    graph.add_node("tool", tool_node)
    graph.add_conditional_edges(
        START,
        route_state,
        {"joke": "joke", "fact": "fact", "tool": "tool"},
    )
    graph.add_edge("joke", END)
    graph.add_edge("fact", END)
    graph.add_edge("tool", END)
    return graph.compile()


def hello_graph(name: str = "student") -> AgentState:
    compiled = build_hello_graph()
    initial_state: AgentState = {"user_message": name}
    if compiled is not None:
        return compiled.invoke(initial_state)
    return {**initial_state, **hello_node(initial_state)}


def conditional_graph(message: str) -> AgentState:
    compiled = build_conditional_graph()
    initial_state: AgentState = {"user_message": message}
    if compiled is not None:
        result = compiled.invoke(initial_state)
        result["route"] = route_message(message)
        return result
    route = route_message(message)
    if route == "joke":
        response = joke_node({})["response"]
    elif route == "tool":
        response = tool_node(initial_state)["response"]
    else:
        response = fact_node({})["response"]
    return {"user_message": message, "route": route, "response": response}


def tool_selection_graph(message: str) -> AgentState:
    lowered = message.lower()
    if "source" in lowered or "triage" in lowered:
        result = source_triage_tool("Official LangGraph documentation updated 2026")
        tool = "source_triage_tool"
    elif "analyze" in lowered or "text" in lowered:
        result = text_analyzer_tool(
            "LangGraph helps students build stateful agent workflows. "
            "State makes each node easier to inspect and test."
        )
        tool = "text_analyzer_tool"
    else:
        result = equation_solver_tool("2*x + 3 = 11")
        tool = "equation_solver_tool"
    return {"user_message": message, "tool_name": tool, "tool_result": result, "response": result}


def human_review_graph(draft: str, approved: bool) -> AgentState:
    response = f"Published: {draft}" if approved else "Paused for human feedback."
    return {"user_message": draft, "approved": approved, "response": response}


def run_research_assistant(question: str, documents: list[str]) -> ResearchState:
    state = ResearchState(question=question, documents=documents)
    state = research_agent(state)
    state = writer_agent(state)
    return reviewer_agent(state)
