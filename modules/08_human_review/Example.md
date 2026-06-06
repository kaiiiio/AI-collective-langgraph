# Module 8 Example: Approval Gate

## Predict

What should happen when `approved` is `True`?

What should happen when `approved` is `False`?

## Run

```powershell
.\lab.cmd module 8
```

## Observe

The same draft has different outcomes:

```text
approved -> publish
not approved -> pause
```

Real workflow version:

```text
open high-risk gaps -> consultant review
resolved gaps -> export submission package
```

## Explain Back

Why is a human review node important in regulated AI systems?
