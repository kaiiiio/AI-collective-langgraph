# Module 6: ReAct Agent Code Walkthrough

## Run

```bash
./lab module 6
```

Windows:

```powershell
.\lab.cmd module 6
```

## Inspect

Start with:

```text
modules/06_agent/main.py
```

Then inspect:

```text
app/graphs/learning_graphs.py
```

## Key Code

```python
def tool_selection_graph(message: str):
    if "solve" in message:
tool = equation_solver_tool
    return {"tool_name": tool_name, "response": result}
```

## Read It In This Order

1. Find the input value.
2. Find the function that receives it.
3. Find the returned state fields.
4. Compare the returned fields with the module output.
