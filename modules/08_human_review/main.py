from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from app.graphs.learning_graphs import human_review_graph

if __name__ == "__main__":
    print(human_review_graph("Draft answer", approved=True))
    print(human_review_graph("Draft answer", approved=False))
