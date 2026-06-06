# AI Collective LangGraph Lab

This repo is a Docker-first LangGraph and LangSmith teaching lab.

## Open These First

- Slides: `docs/slides/index.html`
- Student guide: `docs/student-guide.md`
- Slide outline: `docs/slides/outline.md`
- Speaker script: `docs/slides/speaker-script.md`
- Per-slide instructor notes: `docs/slides/notes/`
- Docker explanation: `docs/docker/README.md`
- LangSmith explanation: `docs/langsmith.md`

## Current Deck Story

The deck starts with two real workflow examples instead of course-unit labels:

1. AI content generation: load business/location context, build prompts, call an AI provider, parse JSON, repair/retry, validate schema, save content, and update bulk progress.
2. VARA licensing workflow: intake, document readiness, indexing, license classification, policy generation, regulatory mapping, gap analysis, human review, export, and remediation.

LangGraph explains how to structure the workflow with state, nodes, and edges. LangSmith explains how to trace, debug, evaluate, and monitor the workflow.

## Run With Docker

```powershell
.\lab.cmd build
.\lab.cmd list
.\lab.cmd module 1
.\lab.cmd module 9
.\lab.cmd capstone
.\lab.cmd test
```

LangSmith settings live in `.env` and are passed into Docker Compose. Do not hardcode keys in Python files.
