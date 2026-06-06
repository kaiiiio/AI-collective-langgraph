# Module 10 Example

Input:

```python
{
    "question": "Why use LangGraph?",
    "documents": ["LangGraph makes stateful workflows explicit."],
}
```

Research node adds:

```python
{"summary": "..."}
```

Writer node adds:

```python
{"draft": "..."}
```

Reviewer node adds:

```python
{"review": "...", "approved": True}
```

This is a compact version of a larger workflow:

```text
input, evidence, specialist roles, review, final output
```

The capstone is not a new idea. It is modules 1 through 9 composed together.
