# Module 5 Example: Conversation Memory

## Predict

If a tutoring assistant answers a question now, what should it remember for the next turn?

## Run

```powershell
.\lab.cmd module 5
```

## Observe

The memory object stores role-tagged messages:

```text
user: What is LangGraph?
assistant: A stateful graph framework.
```

Real workflow version:

```text
consultant: defer this gap
assistant: gap deferred with notes
```

## Explain Back

What is the difference between graph state and longer-lived memory?
