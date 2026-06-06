# Dockerfile Line By Line

The Dockerfile builds the lab image. Think of it as a recipe for a repeatable Python environment.

## Base Image

```dockerfile
FROM python:3.12-slim
```

Start from an official Python image. You do not need to install Python inside the container because the image already contains it.

`slim` means the image is smaller than a full Python image, but still enough for this lab.

## Python Runtime Settings

```dockerfile
ENV PYTHONDONTWRITEBYTECODE=1
```

Do not write `.pyc` files. This keeps the container filesystem simpler and avoids distracting generated files.

```dockerfile
ENV PYTHONUNBUFFERED=1
```

Print logs immediately. When a module runs, output appears right away.

## Working Directory

```dockerfile
WORKDIR /app
```

Set `/app` as the folder inside the container where commands will run.

When Compose later runs:

```text
python modules/01_hello_graph/main.py
```

it runs from `/app`.

## Install Dependencies

```dockerfile
COPY requirements.txt .
```

Copy only the dependency list first. Docker can cache this layer, so dependency installation does not repeat unless `requirements.txt` changes.

```dockerfile
RUN pip install --no-cache-dir -r requirements.txt
```

Install LangGraph, LangSmith, Pydantic, pytest, Ruff, and MyPy into the image.

`--no-cache-dir` keeps the image smaller by not storing pip download cache.

## Copy Project Code

```dockerfile
COPY . .
```

Copy the rest of the repository into `/app`.

The `.dockerignore` file prevents local secrets and generated files from being copied into the image. In this repo, `.env` should be passed at runtime by Compose, not baked into the image.

## Default Command

```dockerfile
CMD ["python", "modules/01_hello_graph/main.py"]
```

This is the default command if someone runs the image directly.

Most lab commands override this through Docker Compose:

```powershell
.\lab.cmd module 3
```

That becomes:

```text
docker compose run --rm lab python modules/03_conditional_edges/main.py
```

## Summary

```text
The Dockerfile builds a repeatable Python environment; Compose chooses which module to run inside it.
```
