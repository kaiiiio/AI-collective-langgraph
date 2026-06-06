# Module 1 Code Walkthrough

## Run

```powershell
.\lab.cmd module 1
```

## Read

Open `modules/01_hello_graph/main.py`.

The important shape is:

```python
def hello_node(state):
    name = state.get("user_message", "student")
    return {"response": f"Hello, {name}. Welcome to LangGraph."}
```

The node reads one field and returns one new field.

## Graph Shape

```text
START -> hello_node -> END
```

This module is intentionally tiny. If you understand the input state, the node return value, and the final merged state, you understand the base pattern for every later module.
