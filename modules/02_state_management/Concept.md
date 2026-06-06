# Module 2: State Management

## Real Scenario

An order flow needs to keep related data together:

```text
order_id
amount
tax
final_amount
invoice
```

That shared object is the graph state.

## Run First

```powershell
.\lab.cmd module 2
```

Expected output:

```text
Before: {'user_message': 'Ada'}
After: {'user_message': 'Ada', 'response': 'Hello, Ada. Welcome to LangGraph.'}
```

## Notice

The original field stayed:

```python
"user_message": "Ada"
```

A new field appeared:

```python
"response": "Hello, Ada. Welcome to LangGraph."
```

## Name The Concept

State is the structured data that moves through a graph run.

For an order workflow, state might look like:

```python
{
    "order_id": "ORD-1001",
    "amount": 500.0,
    "tax": None,
    "final_amount": None,
    "invoice": None,
}
```

Each node should read the fields it needs and return only the fields it changed.

## Check Yourself

Which key existed before the node, and which key appeared after the node?
