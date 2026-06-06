# Module 2 Code Walkthrough

## Run

```powershell
.\lab.cmd module 2
```

## Read

Open `modules/02_state_management/main.py`.

The state type describes the fields the graph may carry:

```python
class AgentState(TypedDict, total=False):
    user_message: str
    response: str
```

`total=False` means every field is optional. A field can appear later after a node returns it.

## Larger Example

The same idea works for an order flow:

```python
class OrderState(TypedDict, total=False):
    order_id: str
    amount: float
    tax: float
    final_amount: float
    invoice: str
```

State lets every node work with one shared object instead of passing many separate variables around.
