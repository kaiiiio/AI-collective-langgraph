# Module-by-Module Teaching Guide

This lab should feel like discovery first and terminology second. Students should run a small graph, inspect what
changed, then name the LangGraph concept they just saw.

Use this rhythm for every module:

1. Ask students to predict what the workflow will do.
2. Run the module with `./lab module <number>` or `.\lab.cmd module <number>`.
3. Read the state before and after the graph runs.
4. Ask which node changed the state.
5. Then introduce the formal term.

## Inductive Teaching Scale

| Label | Meaning |
|---|---|
| Yes | Students can discover the concept mainly by running and inspecting the example. |
| Partly | Start with an example, but add instructor framing because the concept has hidden machinery. |
| No | Better taught by direct explanation first. |

## Module 1: Hello Graph

Command:

```bash
./lab module 1
```

PowerShell:

```powershell
.\lab.cmd module 1
```

How it works: the graph starts with one input state, runs one node, and reaches the end. The node receives the state,
adds or transforms one value, and returns the updated state.

What to teach: this is the smallest possible LangGraph mental model: `START -> node -> END`.

Inductive: **Yes**. Students can see the whole idea by comparing input and output before they know the vocabulary.

## Module 2: State Management

Command:

```bash
./lab module 2
```

How it works: the module makes the state object more explicit. Instead of treating state like a vague dictionary, it
shows which fields are expected and how each node updates only part of the state.

What to teach: state is the shared memory of one graph run. Nodes should read what they need and return only the fields
they changed.

Inductive: **Yes**. Students can infer state by watching values move through the graph.

## Module 3: Conditional Edges

Command:

```bash
./lab module 3
```

How it works: the graph uses a router to choose between branches, such as a joke path or a fact path. The router reads
state and returns the name of the next path.

What to teach: conditional edges are how a graph stops being a fixed chain. The workflow can choose what happens next.

Inductive: **Yes**. Ask students to predict the branch before running it, then confirm the route from the output.

## Module 4: Tools

Command:

```bash
./lab module 4
```

How it works: the graph calls deterministic tools like an equation solver, text analyzer, and source triage helper.
These tools are plain functions that produce reliable results for the graph to use.

What to teach: tools are not magic. A tool is a callable capability outside the model. Start with useful local tools
before adding external APIs, because local tools are easier to inspect, test, and explain.

Inductive: **Yes**. Students can inspect the tool call and result directly.

## Module 5: Memory

Command:

```bash
./lab module 5
```

How it works: the graph keeps conversation history so later turns can use earlier context. The memory helper stores and
retrieves prior messages.

What to teach: memory is state that survives beyond one immediate step. Be clear about the difference between graph-run
state and longer-lived memory.

Inductive: **Yes**. Students can run the example and see the second answer depend on the first interaction.

## Module 6: Agent

Command:

```bash
./lab module 6
```

How it works: the graph follows an agent-like loop: understand the question, choose a tool when needed, use the result,
and form an answer.

What to teach: an agent is a workflow with decision points. The important part is not the word "agent"; it is the
control flow around tool choice and answer generation.

Inductive: **Partly**. Students can observe the flow, but they need instructor framing to separate agent behavior from
ordinary function calls.

## Module 7: Multi-Agent

Command:

```bash
./lab module 7
```

How it works: different nodes represent different roles: researcher, writer, and reviewer. Each role reads the shared
state, contributes its own output, and passes the result forward.

What to teach: multi-agent design is role separation inside a graph. It is useful when each role has a clear job and
the handoff is visible in state.

Inductive: **Partly**. The role handoffs are visible, but students need help seeing why this is still one controlled
graph rather than a group chat.

## Module 8: Human Review

Command:

```bash
./lab module 8
```

How it works: the graph creates a draft, pauses at a review decision, and only publishes when the review state allows it.

What to teach: human-in-the-loop means the graph can include approval, correction, or escalation before continuing.

Inductive: **Yes**. The approval gate is concrete and easy to reason about from the example.

## Module 9: LangSmith

Command:

```bash
./lab module 9
```

How it works: the module runs a graph with LangSmith-ready tracing. With credentials enabled, LangSmith shows the trace,
node runs, inputs, outputs, timing, and errors.

What to teach: LangGraph runs the workflow. LangSmith explains what happened inside the run.

Inductive: **Partly**. The trace UI is observable, but students need a short explanation of traces, spans, and why
observability matters.

## Module 10: Capstone Project

Command:

```bash
./lab capstone
```

How it works: the capstone combines the earlier ideas into a small research assistant: state, nodes, role-specific work,
review, and final output.

What to teach: the capstone is composition, not a new trick. Every part should connect back to a previous module.

Inductive: **Partly**. Students can recognize the pieces, but the instructor should narrate how the modules combine into
one larger workflow.
