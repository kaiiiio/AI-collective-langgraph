# Module 1: Hello Graph Code Walkthrough

## Run

```bash
./lab module 1
```

Windows:

```powershell
.\lab.cmd module 1
```

## Inspect

Start with:

```text
modules/01_hello_graph/main.py
```

Then inspect:

```text
app/graphs/learning_graphs.py
```

## Key Code

```python
def hello_node(state):
    name = state.get("user_message", "student")
    return {"response": f"Hello, {name}. Welcome to LangGraph."}
```

## Read It In This Order

1. Find the input value.
2. Find the function that receives it.
3. Find the returned state fields.
4. Compare the returned fields with the module output.
