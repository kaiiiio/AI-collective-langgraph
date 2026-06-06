# Module 3 Example

Input 1:

```python
{"user_message": "Tell me a joke"}
```

Route:

```text
joke
```

Input 2:

```python
{"user_message": "Tell me a fact"}
```

Route:

```text
fact
```

This is the graph version of an `if` statement.

```text
if state says joke -> joke node
else -> fact node
```

## Try This Mentally

For a support ticket:

```text
refund request -> billing node
password reset -> account node
app crashed -> engineering node
```

What state field would you use to choose the route?
