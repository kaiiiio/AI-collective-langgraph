from __future__ import annotations

from app.state.schemas import ResearchState


def research_agent(state: ResearchState) -> ResearchState:
    joined = " ".join(state.documents) if state.documents else "No documents were provided."
    state.summary = f"Research summary for '{state.question}': {joined}"
    return state


def writer_agent(state: ResearchState) -> ResearchState:
    state.draft = f"Answer: {state.summary}"
    return state


def reviewer_agent(state: ResearchState) -> ResearchState:
    state.review = "Approved because the answer is concise and grounded in the provided context."
    state.approved = True
    return state
