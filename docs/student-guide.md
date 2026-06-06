# Student Guide: LangGraph and LangSmith Lab

This lab teaches LangGraph and LangSmith from real workflow examples.

You do not need to memorize every term first. Start with one question:

```text
What changed in state?
```

## What You Will Learn

By the end, you should be able to explain:

- what graph state is
- what a node receives and returns
- how edges connect steps
- how conditional edges route failures
- where tools, memory, and human review fit
- how LangSmith traces and evaluations help debug workflows

## Open The Slides

Open:

```text
docs/slides/index.html
```

Slide controls:

```text
Right arrow / Space = next slide
Left arrow = previous slide
O = overview
```

## Run The Lab With Docker

Build once:

```powershell
.\lab.cmd build
```

See runnable examples:

```powershell
.\lab.cmd list
```

Run a small graph:

```powershell
.\lab.cmd module 1
```

Run the LangSmith example:

```powershell
.\lab.cmd module 9
```

Run the capstone:

```powershell
.\lab.cmd capstone
```

Run tests:

```powershell
.\lab.cmd test
```

## The Two Main Project Examples

### AI Content Generation

The workflow:

```text
Load business/location data
  -> Build prompt
  -> Call AI provider
  -> Parse JSON
  -> Repair or retry
  -> Validate schema
  -> Save content
  -> Update progress
```

What to notice:

- the model call is only one node
- broken JSON becomes state
- retry logic is a route
- schema validation protects saved content
- progress tracking matters when generating many pages

### VARA Licensing Workflow

The workflow:

```text
Intake
  -> Document readiness
  -> Document indexing
  -> Activity classification
  -> Policy generation
  -> Regulatory mapping
  -> Gap analysis
  -> Human review
  -> Export
```

What to notice:

- evidence should come before classification
- low-confidence AI output should route to review
- human decisions can be stored in graph state
- auditability matters in regulated workflows

## How To Read Code Snippets

For every snippet, ask:

1. What is the state type?
2. What fields does this node read?
3. What fields does this node return?
4. What route happens next?
5. What would LangSmith show in the trace?

## LangSmith Setup

LangSmith settings live in `.env`.

Use this shape:

```text
LANGSMITH_TRACING=true
LANGSMITH_API_KEY=your_key_here
LANGSMITH_PROJECT=langgraph-learning-lab
```

Docker Compose passes those values into the container. Do not hardcode keys in Python.

## What To Remember

LangGraph answers:

```text
What should happen next?
```

LangSmith answers:

```text
What actually happened?
```
