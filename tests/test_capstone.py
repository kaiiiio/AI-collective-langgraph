import unittest

from app.graphs.learning_graphs import run_research_assistant


class CapstoneTests(unittest.TestCase):
    def test_research_assistant_runs_all_roles(self):
        state = run_research_assistant("Why use LangGraph?", ["Stateful workflows", "Branching"])
        self.assertIn("Stateful workflows", state.summary)
        self.assertTrue(state.draft.startswith("Answer:"))
        self.assertTrue(state.approved)
        self.assertIn("Approved", state.review)
