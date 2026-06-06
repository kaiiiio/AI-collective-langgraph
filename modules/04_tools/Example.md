# Module 4 Example: Reliable Tool Results

## Predict

Which tasks should use deterministic code instead of model guessing?

- solve an equation
- count words and keywords
- check if a source looks useful

## Run

```powershell
.\lab.cmd module 4
```

## Observe

Each tool has:

```text
input -> reliable function -> output
```

Real workflow version:

```text
policy text -> section checker -> missing sections
mapping rationale -> citation checker -> needs review?
```

## Explain Back

Why should rule citation checks be tools or validators rather than free-form model text?
