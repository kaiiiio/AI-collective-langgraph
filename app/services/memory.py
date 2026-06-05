from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class ConversationMemory:
    messages: list[str] = field(default_factory=list)

    def add(self, role: str, content: str) -> None:
        self.messages.append(f"{role}: {content}")

    def last(self, count: int = 4) -> list[str]:
        return self.messages[-count:]

    def clear(self) -> None:
        self.messages.clear()
