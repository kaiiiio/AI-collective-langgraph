# Module 3: Conditional Edges

## Real Scenario

A workflow should not always move in a straight line.

For a support ticket:

```text
if billing issue -> billing node
if login issue -> account node
if bug report -> engineering node
```

That is conditional routing.

## Run First

```powershell
.\lab.cmd module 3
```

Expected output:

```text
{'user_message': 'Tell me a joke', 'route': 'joke', 'response': 'A graph node walked into a bar and found the shortest path.'}
{'user_message': 'Tell me a fact', 'route': 'fact', 'response': 'Fact: LangGraph represents workflows as stateful graphs.'}
```

## Notice

The input changes the route:

| Input | Route | Result |
|---|---|---|
| `Tell me a joke` | `joke` | joke response |
| `Tell me a fact` | `fact` | fact response |

## Name The Concept

A conditional edge reads state and chooses the next node.

```python
def route_ticket(state):
    if "billing" in state["message"]:
        return "billing_node"
    return "general_node"
```

## Check Yourself

What value in the input caused the graph to choose a different branch?
