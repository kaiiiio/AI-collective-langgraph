# Module 10: Capstone Project Code Walkthrough

## Run

```bash
./lab capstone
```

Windows:

```powershell
.\lab.cmd capstone
```

## Inspect

Start with:

```text
modules/10_capstone_project/main.py
```

Then inspect:

```text
app/graphs/learning_graphs.py
```

## Key Code

```python
state = ResearchState(question=question, documents=documents)
state = research_agent(state)
state = writer_agent(state)
return reviewer_agent(state)
```

## Read It In This Order

1. Find the input value.
2. Find the function that receives it.
3. Find the returned state fields.
4. Compare the returned fields with the module output.
