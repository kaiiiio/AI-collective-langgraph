# Why Not Simple Chains?

A simple chain is fine for A then B then C. Agents often need branching, memory, retries, review, and persistence.

```mermaid
graph TD
    A["Concept"] --> B["Code"]
    B --> C["Example"]
    C --> D["Exercise"]
    D --> E["Solution"]
```

## Instructor Notes

Start with the mental model, draw the graph, run the smallest possible example, then ask students to change
one thing. The repetition is intentional: concept, code, example, exercise, solution.
