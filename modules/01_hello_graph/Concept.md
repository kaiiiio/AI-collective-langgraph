# Module 1: Hello Graph

## Real Scenario

Start with the smallest possible workflow:

```text
input state -> one node -> output state
```

Imagine a tiny onboarding flow. A name enters the system, and the workflow adds one greeting.

## Run First

```powershell
.\lab.cmd module 1
```

Expected output:

```text
{'user_message': 'student', 'response': 'Hello, student. Welcome to LangGraph.'}
```

## Notice

Before the node runs, the state has:

```python
{"user_message": "student"}
```

After the node runs, the state also has:

```python
{"response": "Hello, student. Welcome to LangGraph."}
```

## Name The Concept

A LangGraph workflow can be as small as:

```text
START -> node -> END
```

The node is just a function:

```python
def hello_node(state):
    return {"response": "Hello, student. Welcome to LangGraph."}
```

## Check Yourself

What did the node receive, and what did it return?
