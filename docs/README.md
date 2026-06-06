# Student Learning Index

This lab teaches LangGraph from real workflows first. Do not start by memorizing agent vocabulary. Start by watching data move.

## The First Mental Model

An AI workflow is usually more than one prompt:

```text
Load context -> Build prompt -> Call model -> Parse output -> Validate -> Save
```

A LangGraph workflow gives those steps names and passes one shared state object through them.

```text
START -> Node A -> Node B -> Router -> Node C -> END
```

Every node follows the same pattern:

```python
def some_node(state):
    # Read current state.
    # Do one bounded task.
    # Return only the fields that changed.
    return {"field_that_changed": new_value}
```

LangGraph merges the returned update into the existing state.

## Project Flow 1: AI Content Generation

This workflow generates business or location pages at scale:

```text
Start content request
  -> Fetch company, suburb, or province data
  -> Build structured SEO prompt
  -> Call OpenAI or Gemini provider
  -> Parse JSON response
  -> Repair or retry if broken
  -> Enforce expected schema
  -> Save generated content
  -> Update bulk job progress
  -> End
```

The important lesson is that the model call is only one node. The system also needs context loading, parsing, retry routes, schema gates, saving, and progress tracking.

## Project Flow 2: VARA Licensing Workflow

This workflow prepares a regulated licensing case:

```text
Client intake
  -> Required document readiness
  -> Document indexing and retrieval prep
  -> License activity classification
  -> Policy generation
  -> Operational diagram generation
  -> Regulatory mapping
  -> Gap analysis
  -> Human gap decisions
  -> Submission package export
  -> Feedback and remediation
```

The important lesson is that regulated AI needs evidence, review checkpoints, auditability, and human judgment.

## How To Read Any Example

Use the same loop every time:

1. Name the state fields.
2. Find the node function.
3. Ask what the node reads from state.
4. Ask what update the node returns.
5. Find the edge or conditional route.
6. Run the example.
7. Change one input and compare what changed in state.

## Where The Teaching Materials Live

| File | Purpose |
|---|---|
| `docs/slides/index.html` | Main slide deck. |
| `docs/slides/outline.md` | Slide-by-slide structure. |
| `docs/slides/speaker-script.md` | Instructor talk track for every slide. |
| `docs/slides/notes/` | Instructor notes for every slide. |
| `docs/student-guide.md` | Student-facing guide and run path. |
| `docs/docker/README.md` | Docker setup explained for students. |
| `docs/langsmith.md` | LangSmith tracing, debugging, and evaluation notes. |

## Student Start Path

Students should open these in order:

1. `docs/student-guide.md`
2. `docs/slides/index.html`
3. `docs/docker/README.md`
4. `docs/langsmith.md`

The instructor script is intentionally separate from the visible slides:

```text
docs/slides/speaker-script.md
```

## Docker Path

Run everything through Docker first:

```powershell
.\lab.cmd build
.\lab.cmd list
.\lab.cmd module 1
.\lab.cmd module 9
.\lab.cmd capstone
.\lab.cmd test
```

Docker keeps Python, dependencies, and LangSmith environment variables stable, so students can focus on the graph.

## What To Remember

When confused, return to one question:

```text
What did this node receive, and what did it return?
```

If students can answer that for each node, they can understand the whole workflow.
