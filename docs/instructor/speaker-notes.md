# Speaker Notes

Keep each explanation grounded in one question: what changed in state?

For every module:

1. Draw the graph.
2. Identify each node.
3. Identify each edge.
4. Show the state before execution.
5. Run the code.
6. Show the state after execution.
7. Ask students to modify one thing.

Run modules with the short launcher:

```bash
./lab module 1
```

PowerShell:

```powershell
.\lab.cmd module 1
```

LangSmith section: explain that a trace is the whole graph run, spans/runs are the individual operations, and
metrics make slow or expensive nodes visible.
