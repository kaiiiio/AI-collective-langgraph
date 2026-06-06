# Module 2 Example

Start state:

```python
{"user_message": "Ada"}
```

Node return value:

```python
{"response": "Hello, Ada. Welcome to LangGraph."}
```

Final state:

```python
{
    "user_message": "Ada",
    "response": "Hello, Ada. Welcome to LangGraph.",
}
```

The pattern to look for in every module:

```text
state before node
node returns a partial update
LangGraph merges the update into state
```

## Try This Mentally

If an order starts as:

```python
{"order_id": "ORD-1", "amount": 100}
```

and a tax node returns:

```python
{"tax": 18}
```

the merged state is:

```python
{"order_id": "ORD-1", "amount": 100, "tax": 18}
```
