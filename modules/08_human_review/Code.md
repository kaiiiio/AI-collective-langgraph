# Module 8: Human Review Code Walkthrough

## Run

```bash
./lab module 8
```

Windows:

```powershell
.\lab.cmd module 8
```

## Inspect

Start with:

```text
modules/08_human_review/main.py
```

Then inspect:

```text
app/graphs/learning_graphs.py
```

## Key Code

```python
def human_review_graph(draft: str, approved: bool):
    response = f"Published: {draft}" if approved else "Paused for human feedback."
```

## Read It In This Order

1. Find the input value.
2. Find the function that receives it.
3. Find the returned state fields.
4. Compare the returned fields with the module output.
