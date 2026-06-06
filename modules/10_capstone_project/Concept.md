# Module 10: Capstone Project

## Real Scenario

The capstone is a compact version of a complete AI workflow.

The example is a research assistant:

```text
question -> evidence -> specialist roles -> review -> final output
```

## Run First

```powershell
.\lab.cmd capstone
```

Expected output:

```text
{'question': 'Why use LangGraph?', 'documents': [...], 'summary': ..., 'draft': ..., 'review': ..., 'approved': True}
```

## Notice

Every output field connects to a previous concept:

| Field | Concept |
|---|---|
| `question` | initial state |
| `documents` | input evidence |
| `summary` | research node |
| `draft` | writer node |
| `review` | reviewer node |
| `approved` | review decision |

## Name The Concept

Composition means building a larger workflow from smaller understandable parts.

Production-style AI systems stay debuggable when they have:

1. explicit state
2. small nodes
3. visible routes
4. reliable tools
5. human approval gates
6. LangSmith traces

## Check Yourself

Which earlier module explains each field in the capstone state?
