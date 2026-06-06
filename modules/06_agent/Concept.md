# Module 6: Agent Loop

## Real Scenario

An AI workflow often needs to decide what action comes next.

For a support assistant:

- if the request asks for exact math, call a calculator tool
- if the request asks about text, call a text analyzer
- if the request asks about a source, call a source triage tool
- after the tool returns, write the response

## Run First

```powershell
.\lab.cmd module 6
```

Expected output:

```text
{'user_message': 'solve an equation', 'tool_name': 'equation_solver_tool', 'tool_result': 'x = 4', 'response': 'x = 4'}
{'user_message': 'analyze this text', 'tool_name': 'text_analyzer_tool', ...}
{'user_message': 'triage this source', 'tool_name': 'source_triage_tool', ...}
```

## Notice

Different requests choose different tools.

That is the agent loop in a small form:

```text
decide -> act -> observe -> answer
```

## Name The Concept

An agent is not magic. It is a workflow that uses current state to choose an action.

```python
if "triage" in state["user_message"]:
    tool_name = "source_triage_tool"
```

## Check Yourself

Where do you see the decision, the action, and the observation in the output?
