# Module 8: Human Review Example

## Predict

Before running the module, predict the final state.

Ask:

- What is the starting input?
- Which step runs first?
- What new key or value should appear?

## Run

```bash
./lab module 8
```

## Observe

- `approved=True` publishes the draft.
- `approved=False` pauses the workflow.
- The decision is explicit in state.
- This pattern is useful for risky or high-impact outputs.

## Explain Back

In one sentence, explain what changed and why.
