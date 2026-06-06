# Module 10 Code Walkthrough

## Run

```powershell
.\lab.cmd capstone
```

## Read

Open `app/graphs/learning_graphs.py`:

```python
def run_research_assistant(question: str, documents: list[str]):
    state = ResearchState(question=question, documents=documents)
    state = research_agent(state)
    state = writer_agent(state)
    return reviewer_agent(state)
```

Then open `app/state/schemas.py`:

```python
class ResearchState(BaseModel):
    question: str
    documents: list[str]
    summary: str = ""
    draft: str = ""
    review: str = ""
    approved: bool = False
```

## Workflow Translation

The same architecture can scale to many domains:

```text
input
  -> gather evidence
  -> specialist role
  -> draft output
  -> review
  -> final response
```

The capstone is small on purpose so you can see every state field and every role.
