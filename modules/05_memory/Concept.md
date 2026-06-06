# Module 5: Memory

## Real Scenario

A conversation usually does not finish in one message.

Someone may ask a question, receive an answer, and then ask a follow-up:

```text
What is LangGraph?
Can you give me a smaller example?
How does state change after each node?
```

The workflow needs useful context from earlier turns.

## Run First

```powershell
.\lab.cmd module 5
```

Expected output:

```text
['user: What is LangGraph?', 'assistant: A stateful graph framework.']
```

## Notice

The memory stores prior messages so the next step can use them.

State is the data for one graph run. Memory is context that can survive beyond one immediate step.

## Name The Concept

Memory lets a workflow carry useful history:

```python
memory.add("user", "What is LangGraph?")
memory.add("assistant", "A stateful graph framework.")
history = memory.last(4)
```

In larger systems, memory may be backed by a database, checkpoint store, or conversation history service.

## Check Yourself

What would the assistant lose if it had no memory?
