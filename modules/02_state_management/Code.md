# Module 2: State Management Code Walkthrough

## Run

```bash
./lab module 2
```

Windows:

```powershell
.\lab.cmd module 2
```

## Inspect

Start with:

```text
modules/02_state_management/main.py
```

Then inspect:

```text
modules/02_state_management/main.py
```

## Key Code

```python
before = {"user_message": "Ada"}
after = hello_graph(before["user_message"])
```

## Read It In This Order

1. Find the input value.
2. Find the function that receives it.
3. Find the returned state fields.
4. Compare the returned fields with the module output.
