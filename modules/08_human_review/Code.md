# Module 8 Code Walkthrough

## Run

```powershell
.\lab.cmd module 8
```

## Read

Find `human_review_graph` in `app/graphs/learning_graphs.py`:

```python
def human_review_graph(draft: str, approved: bool):
    response = f"Published: {draft}" if approved else "Paused for human feedback."
    return {"user_message": draft, "approved": approved, "response": response}
```

## Real Workflow Translation

```python
def route_after_gap_review(state):
    if state["review_complete"] and not state["open_gaps"]:
        return "export_submission"
    return "remediation"
```

Human approval is a routing input.
