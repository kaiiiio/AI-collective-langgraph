from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from app.graphs.learning_graphs import tool_selection_graph

if __name__ == "__main__":
    print(tool_selection_graph("solve an equation"))
    print(tool_selection_graph("analyze this text"))
    print(tool_selection_graph("triage this source"))
