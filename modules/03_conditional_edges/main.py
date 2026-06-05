from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from app.graphs.learning_graphs import conditional_graph

if __name__ == "__main__":
    print(conditional_graph("Tell me a joke"))
    print(conditional_graph("Tell me a fact"))
