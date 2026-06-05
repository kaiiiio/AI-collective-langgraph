# Module 9: LangSmith Code Walkthrough

## Run

```bash
./lab module 9
```

Windows:

```powershell
.\lab.cmd module 9
```

## Inspect

Start with:

```text
modules/09_langsmith/main.py
```

Then inspect:

```text
app/config/settings.py
```

## Key Code

```python
LANGSMITH_TRACING=true
LANGSMITH_API_KEY=your_key
LANGSMITH_PROJECT=langgraph-learning-lab
```

## Read It In This Order

1. Find the input value.
2. Find the function that receives it.
3. Find the returned state fields.
4. Compare the returned fields with the module output.
