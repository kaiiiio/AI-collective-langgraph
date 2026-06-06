# Docker Compose Line By Line

Docker Compose names the jobs we need.

This repo has two services:

```text
lab  -> runs modules and capstone demos
test -> runs pytest in the same environment
```

## Services

```yaml
services:
```

Start the list of runnable jobs.

## Lab Service

```yaml
  lab:
```

Define the service used for module demos.

When you run:

```powershell
.\lab.cmd module 1
```

PowerShell eventually calls:

```text
docker compose run --rm lab python modules/01_hello_graph/main.py
```

## Build

```yaml
    build: .
```

Build the image from the `Dockerfile` in the repository root.

The dot means:

```text
use this project folder as the build context
```

## Environment

```yaml
    environment:
      LANGSMITH_TRACING: ${LANGSMITH_TRACING:-false}
      LANGSMITH_API_KEY: ${LANGSMITH_API_KEY:-}
      LANGSMITH_PROJECT: ${LANGSMITH_PROJECT:-langgraph-learning-lab}
```

Pass LangSmith settings into the container.

Compose reads `.env` automatically. If `.env` has:

```text
LANGSMITH_TRACING=true
LANGSMITH_API_KEY=...
LANGSMITH_PROJECT=langgraph-learning-lab
```

then the container receives those values as environment variables.

The `:-default` part means the lab still runs even when `.env` does not exist.

## Default Lab Command

```yaml
    command: python modules/10_capstone_project/main.py
```

Set the default command for the `lab` service to the capstone.

The wrapper script can override it for individual modules:

```powershell
.\lab.cmd module 4
```

## Test Service

```yaml
  test:
```

Define the service used for automated checks.

```yaml
    build: .
```

Use the same image as the lab service.

```yaml
    environment:
      LANGSMITH_TRACING: ${LANGSMITH_TRACING:-false}
      LANGSMITH_API_KEY: ${LANGSMITH_API_KEY:-}
      LANGSMITH_PROJECT: ${LANGSMITH_PROJECT:-langgraph-learning-lab}
```

Give tests the same environment shape as the lab. That means tests and demos run under the same configuration.

```yaml
    command: python -m pytest -q
```

Run the test suite quietly.

## Summary

```text
Compose turns the Docker image into named jobs: one for modules, one for tests, both with the same LangSmith config.
```
