# Module 4: Tools

## Real Scenario

A model should not guess work that normal software can do exactly.

Use tools for reliable tasks:

- calculate values
- count words
- check a URL or source label
- validate required fields
- format output

## Run First

```powershell
.\lab.cmd module 4
```

Expected output:

```text
x = 4
words=8; sentences=2; reading_time=1 min; keywords=langgraph, keeps, state
high-priority: primary-source signal, freshness signal
```

## Notice

Each result came from deterministic code, not model guessing.

| Tool | Simple meaning |
|---|---|
| `equation_solver_tool` | Solve a small exact equation. |
| `text_analyzer_tool` | Count and summarize text features. |
| `source_triage_tool` | Label source quality signals. |

## Name The Concept

A tool is a callable capability outside the model.

```python
def source_triage_tool(source):
    if "official" in source.lower():
        return "high-priority"
    return "needs verification"
```

The graph stores the tool result as an observation in state.

## Check Yourself

Which output would be risky for a model to guess without a tool?
