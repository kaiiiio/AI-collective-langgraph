# Dockerfile Line By Line

```dockerfile
FROM python:3.12-slim
```

Starts from a small official Python image. Students do not need Python installed locally inside the container.

```dockerfile
ENV PYTHONDONTWRITEBYTECODE=1
```

Stops Python from writing `.pyc` files. This keeps the container filesystem quieter.

```dockerfile
ENV PYTHONUNBUFFERED=1
```

Prints logs immediately instead of buffering them. This is useful for workshops and production logs.

```dockerfile
WORKDIR /app
```

Sets `/app` as the working directory inside the container.

```dockerfile
COPY requirements.txt .
```

Copies dependency definitions first so Docker can cache dependency installation.

```dockerfile
RUN pip install --no-cache-dir -r requirements.txt
```

Installs Python dependencies without keeping pip cache files.

```dockerfile
COPY . .
```

Copies the rest of the repository into the image.

```dockerfile
CMD ["python", "modules/01_hello_graph/main.py"]
```

Defines the default command when the container starts.
