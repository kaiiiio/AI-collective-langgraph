import unittest

from app.services.memory import ConversationMemory


class MemoryTests(unittest.TestCase):
    def test_memory_returns_recent_messages(self):
        memory = ConversationMemory()
        memory.add("user", "one")
        memory.add("assistant", "two")
        memory.add("user", "three")
        self.assertEqual(memory.last(2), ["assistant: two", "user: three"])

    def test_memory_clear_removes_messages(self):
        memory = ConversationMemory(["user: hello"])
        memory.clear()
        self.assertEqual(memory.messages, [])
