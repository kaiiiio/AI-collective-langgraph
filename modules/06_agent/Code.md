# Module 6 Code Walkthrough

## Run

```powershell
.\lab.cmd module 6
```

## Read

Find `tool_selection_graph` in `app/graphs/learning_graphs.py`:

```python
def tool_selection_graph(message: str):
    lowered = message.lower()
    if "source" in lowered or "triage" in lowered:
        result = source_triage_tool(...)
        tool = "source_triage_tool"
    elif "analyze" in lowered or "text" in lowered:
        result = text_analyzer_tool(...)
        tool = "text_analyzer_tool"
    else:
        result = equation_solver_tool(...)
        tool = "equation_solver_tool"
    return {"tool_name": tool, "tool_result": result, "response": result}
```

## Real Workflow Translation

```text
case needs evidence check -> source triage tool
case needs policy check -> policy section checker
case needs package check -> submission validator
```
