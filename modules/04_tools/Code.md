# Module 4: Tools Code Walkthrough

## Run

```bash
./lab module 4
```

Windows:

```powershell
.\lab.cmd module 4
```

## Inspect

Start with:

```text
modules/04_tools/main.py
```

Then inspect:

```text
app/tools/basic_tools.py
```

## Key Code

```python
def equation_solver_tool(equation: str) -> str:
    return "x = 4"
```

## Read It In This Order

1. Find the input value.
2. Find the function that receives it.
3. Find the returned state fields.
4. Compare the returned fields with the module output.
