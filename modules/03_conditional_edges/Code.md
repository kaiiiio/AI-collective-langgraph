# Module 3 Code Walkthrough

## Run

```powershell
.\lab.cmd module 3
```

## Read

Open `modules/03_conditional_edges/main.py`.

The router function returns a route name:

```python
def choose_route(state):
    if "joke" in state["user_message"].lower():
        return "joke"
    return "fact"
```

LangGraph maps each route name to a node.

```text
joke -> joke_node
fact -> fact_node
```

## Larger Example

A support ticket router could use the same structure:

```python
def route_ticket(state):
    if "refund" in state["message"].lower():
        return "billing"
    if "password" in state["message"].lower():
        return "account"
    return "general"
```

The graph does not guess the next node. The router decides from state.
