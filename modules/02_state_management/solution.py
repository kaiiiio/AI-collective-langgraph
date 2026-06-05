from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from app.graphs.learning_graphs import hello_graph

if __name__ == "__main__":
    before = {"user_message": "Ada"}
    print("Before:", before)
    after = hello_graph(before["user_message"])
    print("After:", after)
