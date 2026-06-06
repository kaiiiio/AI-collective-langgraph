# Module 8: Human Review

## Real Scenario

Some workflows should pause before publishing, sending, refunding, deleting, or submitting anything important.

AI can draft or recommend, but a human can own the final decision.

## Run First

```powershell
.\lab.cmd module 8
```

Expected output:

```text
{'user_message': 'Draft answer', 'approved': True, 'response': 'Published: Draft answer'}
{'user_message': 'Draft answer', 'approved': False, 'response': 'Paused for human feedback.'}
```

## Notice

The same draft has two different outcomes because approval changed.

## Name The Concept

Human-in-the-loop means the workflow can pause, wait for a decision, and continue only when the state allows it.

```python
if state["approved"]:
    return {"response": "Published"}
return {"response": "Paused for human feedback"}
```

## Check Yourself

Why should an important action be blocked when approval is false?
