from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from app.config import Settings
from app.graphs.learning_graphs import hello_graph

if __name__ == "__main__":
    settings = Settings()
    print({"tracing": settings.langsmith_tracing, "project": settings.langsmith_project})
    print(hello_graph("LangSmith learner"))
