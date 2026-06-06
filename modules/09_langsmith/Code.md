# Module 9 Code Walkthrough

## Run

```powershell
.\lab.cmd module 9
```

## Read

Open `modules/09_langsmith/main.py`:

```python
settings = Settings()
print({"tracing": settings.langsmith_tracing, "project": settings.langsmith_project})
print(hello_graph("LangSmith learner"))
```

Open `app/config/settings.py`:

```python
langsmith_tracing: bool = Field(default=False, alias="LANGSMITH_TRACING")
langsmith_api_key: str | None = Field(default=None, alias="LANGSMITH_API_KEY")
langsmith_project: str = Field(default="langgraph-learning-lab", alias="LANGSMITH_PROJECT")
```

## Real Workflow Translation

```text
.env -> docker compose -> container environment -> Settings -> LangSmith trace
```

For regulated workflows, traces help prove why a decision was made.
