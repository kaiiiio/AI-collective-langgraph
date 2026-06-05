# Module 5: Memory Code Walkthrough

## Run

```bash
./lab module 5
```

Windows:

```powershell
.\lab.cmd module 5
```

## Inspect

Start with:

```text
modules/05_memory/main.py
```

Then inspect:

```text
app/services/memory.py
```

## Key Code

```python
memory.add("user", "What is LangGraph?")
memory.add("assistant", "A stateful graph framework.")
print(memory.last(2))
```

## Read It In This Order

1. Find the input value.
2. Find the function that receives it.
3. Find the returned state fields.
4. Compare the returned fields with the module output.
