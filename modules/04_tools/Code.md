# Module 4 Code Walkthrough

## Run

```powershell
.\lab.cmd module 4
```

## Read

Open `app/tools/basic_tools.py`.

Focus on tool shape:

```python
def text_analyzer_tool(text: str) -> str:
    words = ...
    return f"words={len(words)}; ..."
```

Tools should be:

- clear
- testable
- deterministic when possible
- safe to call from a graph node

## Real Workflow Translation

```python
def policy_section_checker(policy_text: str) -> dict:
    return {
        "has_governance": "governance" in policy_text.lower(),
        "has_monitoring": "monitoring" in policy_text.lower(),
        "has_recordkeeping": "record" in policy_text.lower(),
    }
```
