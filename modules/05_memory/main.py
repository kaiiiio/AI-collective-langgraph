from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from app.services.memory import ConversationMemory

if __name__ == "__main__":
    memory = ConversationMemory()
    memory.add("user", "What is LangGraph?")
    memory.add("assistant", "A stateful graph framework.")
    print(memory.last(2))
