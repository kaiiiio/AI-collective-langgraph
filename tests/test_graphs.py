import unittest

from app.graphs.learning_graphs import conditional_graph, hello_graph, human_review_graph, route_message


class GraphTests(unittest.TestCase):
    def test_hello_graph_returns_response(self):
        self.assertEqual(hello_graph("Ada")["response"], "Hello, Ada. Welcome to LangGraph.")

    def test_route_message_selects_joke_branch(self):
        self.assertEqual(route_message("Tell me a joke"), "joke")

    def test_conditional_graph_returns_fact_for_default_route(self):
        result = conditional_graph("What is LangGraph?")
        self.assertEqual(result["route"], "fact")
        self.assertIn("stateful graphs", result["response"])

    def test_human_review_pauses_when_not_approved(self):
        self.assertEqual(
            human_review_graph("Draft", approved=False)["response"],
            "Paused for human feedback.",
        )
