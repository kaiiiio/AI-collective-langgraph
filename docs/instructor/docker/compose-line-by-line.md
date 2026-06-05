# Docker Compose Line By Line

```yaml
services:
```

Starts the list of runnable services.

```yaml
  lab:
```

Defines one service named `lab`.

```yaml
    build: .
```

Builds the image from the Dockerfile in the repository root.

```yaml
    environment:
      LANGSMITH_TRACING: ${LANGSMITH_TRACING:-false}
      LANGSMITH_API_KEY: ${LANGSMITH_API_KEY:-}
      LANGSMITH_PROJECT: ${LANGSMITH_PROJECT:-langgraph-learning-lab}
```

Passes LangSmith settings into the container. The values come from `.env` when it exists, and otherwise use safe
defaults so the lab runs immediately.

```yaml
    command: python modules/10_capstone_project/main.py
```

Overrides the Dockerfile default command so Compose runs the capstone demo.
