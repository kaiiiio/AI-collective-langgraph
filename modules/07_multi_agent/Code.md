# Module 7: Multi-Agent Code Walkthrough

## Run

```bash
./lab module 7
```

Windows:

```powershell
.\lab.cmd module 7
```

## Inspect

Start with:

```text
modules/07_multi_agent/main.py
```

Then inspect:

```text
app/agents/research_team.py
```

## Key Code

```python
state = research_agent(state)
state = writer_agent(state)
state = reviewer_agent(state)
```

## Read It In This Order

1. Find the input value.
2. Find the function that receives it.
3. Find the returned state fields.
4. Compare the returned fields with the module output.
