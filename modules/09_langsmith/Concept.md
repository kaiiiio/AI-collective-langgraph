# Module 9: LangSmith

## Real Scenario

Suppose a question-answering workflow gives a weak answer. You need to know:

```text
Which node ran?
What state entered that node?
What did the node return?
Which tool or model call happened inside it?
Where did the answer first become wrong?
```

Logs are not enough. You need traces.

## Run First

```powershell
.\lab.cmd module 9
```

Expected output:

```text
{'tracing': True, 'project': 'langgraph-learning-lab'}
{'user_message': 'LangSmith learner', 'response': 'Hello, LangSmith learner. Welcome to LangGraph.'}
```

## Notice

LangSmith is the observability layer.

It can show:

- the full graph run
- node inputs
- node outputs
- tool calls
- model calls
- errors
- latency and token usage

## Name The Concept

LangGraph runs the workflow. LangSmith shows what happened inside it.

```python
from langsmith import traceable

@traceable(name="Generate answer")
def generate_answer(question, evidence):
    ...
```

## Check Yourself

Where would you look to prove which node made the wrong decision?
