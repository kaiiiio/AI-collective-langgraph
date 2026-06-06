# Module 5 Code Walkthrough

## Run

```powershell
.\lab.cmd module 5
```

## Read

Open `modules/05_memory/main.py`.

The memory object stores entries:

```python
memory.add("user", "What is LangGraph?")
memory.add("assistant", "A stateful graph framework.")
```

Then it can return recent history:

```python
memory.last(4)
```

## Larger Example

For a study assistant, memory-like data could include:

```text
last question
previous answer
topics already explained
examples the learner understood
```

The module keeps the implementation small so the pattern is visible.
