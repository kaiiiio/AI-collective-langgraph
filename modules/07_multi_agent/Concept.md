# Module 7: Multi-Agent Roles

## Real Scenario

A serious AI workflow should not be one giant step doing everything.

For a question-answering assistant, separate roles might handle:

- research
- summarizing
- drafting
- reviewing
- approval

Each role should have a bounded task and a visible output.

## Run First

```powershell
.\lab.cmd module 7
```

Expected output:

```text
{'question': 'What is LangGraph?', 'documents': ['LangGraph is a stateful graph framework.'], 'summary': ..., 'draft': ..., 'review': ..., 'approved': True}
```

## Notice

Different fields come from different roles:

| Role | Field It Produces |
|---|---|
| Researcher | `summary` |
| Writer | `draft` |
| Reviewer | `review`, `approved` |

## Name The Concept

Multi-agent can mean role-based graph nodes.

```text
researcher -> writer -> reviewer
```

This is easier to debug than one giant prompt because each role has a clear contract.

## Check Yourself

Which role wrote each field in the final state?
