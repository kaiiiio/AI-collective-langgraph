# Module 1 Example: One Step Workflow

## Predict

Before running, predict the final state:

```python
{"user_message": "student"}
```

What new field should appear after the graph runs?

## Run

```powershell
.\lab.cmd module 1
```

## Observe

The node reads `user_message` and returns `response`.

```text
START -> hello_node -> END
```

## Explain Back

In one sentence: a graph node receives state and returns a state update.
