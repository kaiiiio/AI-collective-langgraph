# Module 3: Conditional Edges Code Walkthrough

## Run

```bash
./lab module 3
```

Windows:

```powershell
.\lab.cmd module 3
```

## Inspect

Start with:

```text
modules/03_conditional_edges/main.py
```

Then inspect:

```text
app/graphs/learning_graphs.py
```

## Key Code

```python
def route_message(message: str) -> str:
    if "joke" in message.lower():
return "joke"
    return "fact"
```

## Read It In This Order

1. Find the input value.
2. Find the function that receives it.
3. Find the returned state fields.
4. Compare the returned fields with the module output.
