# Module 9 Example

Without tracing, you might only see:

```text
Final answer was weak.
```

With LangSmith, you can inspect:

```text
graph run
  node input
  node output
  tool call
  model call
  error or latency
```

Useful debugging questions:

```text
Which node changed the answer?
Which input was missing?
Which tool returned surprising data?
Which model call was slow?
```

The trace turns a vague failure into a specific place to inspect.
