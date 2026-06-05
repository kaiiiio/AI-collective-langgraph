from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from app.graphs.learning_graphs import run_research_assistant

if __name__ == "__main__":
    state = run_research_assistant("Why use LangGraph?", ["It supports state.", "It supports branching and observability."])
    print(state.model_dump())
