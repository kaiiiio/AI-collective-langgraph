from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from app.tools import equation_solver_tool, source_triage_tool, text_analyzer_tool

if __name__ == "__main__":
    print(equation_solver_tool("2*x + 3 = 11"))
    print(text_analyzer_tool("LangGraph keeps state visible. Tools keep work testable."))
    print(source_triage_tool("Official LangGraph documentation updated 2026"))
