# Module 7 Code Walkthrough

## Run

```powershell
.\lab.cmd module 7
```

## Read

Open `modules/07_multi_agent/main.py`.

The workflow calls role-specific functions:

```python
state = research_agent(state)
state = writer_agent(state)
state = reviewer_agent(state)
```

Each role reads the shared state and returns a focused update.

## Larger Example

A document workflow could use the same role pattern:

```text
researcher -> drafter -> editor -> reviewer -> publisher
```

The important idea is not the role names. The important idea is that each role has one job and one visible output.
