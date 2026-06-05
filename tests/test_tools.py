import unittest

from app.tools import equation_solver_tool, source_triage_tool, text_analyzer_tool


class ToolTests(unittest.TestCase):
    def test_equation_solver_solves_linear_equation(self):
        self.assertEqual(equation_solver_tool("2*x + 3 = 11"), "x = 4")

    def test_equation_solver_rejects_unsafe_expression(self):
        with self.assertRaises(ValueError):
            equation_solver_tool("__import__('os').system('echo unsafe') = 1")

    def test_text_analyzer_returns_metrics(self):
        result = text_analyzer_tool("LangGraph keeps state visible. Tools keep work testable.")
        self.assertIn("words=8", result)
        self.assertIn("keywords=langgraph", result)

    def test_source_triage_prioritizes_primary_sources(self):
        result = source_triage_tool("Official GitHub documentation updated 2026")
        self.assertIn("high-priority", result)
