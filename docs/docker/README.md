# Docker For This Lab

Docker is the repeatability layer for the LangGraph and LangSmith lab.

The point is not to learn Docker for its own sake. The point is to make every student run the same Python version, the same packages, and the same environment variables.

## The Problem Docker Solves

Without Docker, a student can get blocked before they ever see a graph run:

```text
wrong Python version
missing dependency
broken virtual environment
different shell behavior
LangSmith key loaded in one terminal but not another
```

With Docker, the lab runs inside a packaged environment:

```text
Dockerfile -> image -> container -> graph demo output
```

## Image vs Container

An image is the packaged environment:

```text
Python 3.12
LangGraph
LangSmith
Pydantic
pytest
repo source files
```

A container is one live run of that image:

```text
run a graph example
run the LangSmith tracing example
run the capstone demo
run tests
```

Build the image once. Run containers many times.

## How The Wrapper Works

Students type a short command:

```powershell
.\lab.cmd module 9
```

The wrapper sends the real work to Docker Compose:

```text
lab.cmd
  -> lab.ps1
  -> docker compose run --rm lab ...
```

The important part is `--rm`: each run is temporary. Students get a clean run instead of a long-lived container full of old state.

## LangSmith Environment Flow

LangSmith configuration should live in `.env`, not inside Python code.

```text
.env
  -> docker compose
  -> container environment
  -> Python settings
  -> LangSmith trace
```

Use these variable names:

```text
LANGSMITH_TRACING=true
LANGSMITH_API_KEY=...
LANGSMITH_PROJECT=langgraph-learning-lab
```

Docker Compose reads `.env` automatically and passes the values into the `lab` and `test` services.

## Commands Students Need

```powershell
.\lab.cmd build
.\lab.cmd list
.\lab.cmd module 1
.\lab.cmd module 9
.\lab.cmd capstone
.\lab.cmd test
.\lab.cmd down
```

| Command | Meaning |
|---|---|
| `build` | Create the Docker image from the Dockerfile. |
| `list` | Show the runnable examples. |
| `module 1` | Run the first small LangGraph example. |
| `module 9` | Run the LangSmith tracing example with `.env` settings. |
| `capstone` | Run the larger composed workflow demo. |
| `test` | Run pytest in the same Docker image. |
| `down` | Stop and clean Compose resources. |

## Instructor Explanation

Say this in class:

> Docker is not the graph. Docker is the classroom setup. It makes sure everyone starts from the same environment, then LangGraph and LangSmith are the ideas we study inside that environment.

Then run one small graph example and ask students:

```text
What changed in state during this run?
```
