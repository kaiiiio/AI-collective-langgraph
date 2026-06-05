from __future__ import annotations

from dataclasses import dataclass, field
from typing import Literal, TypedDict

try:
    from pydantic import BaseModel, Field
    HAS_PYDANTIC = True
except ModuleNotFoundError:
    HAS_PYDANTIC = False
    BaseModel = object

    def Field(default_factory):
        return field(default_factory=default_factory)


class AgentState(TypedDict, total=False):
    user_message: str
    route: Literal["joke", "fact", "tool", "answer"]
    response: str
    tool_name: str
    tool_result: str
    history: list[str]
    approved: bool


if HAS_PYDANTIC:

    class ResearchState(BaseModel):
        question: str
        documents: list[str] = Field(default_factory=list)
        summary: str = ""
        draft: str = ""
        review: str = ""
        approved: bool = False

else:

    @dataclass
    class ResearchState(BaseModel):
        question: str
        documents: list[str] = Field(default_factory=list)
        summary: str = ""
        draft: str = ""
        review: str = ""
        approved: bool = False

        def model_dump(self) -> dict[str, object]:
            return {
                "question": self.question,
                "documents": self.documents,
                "summary": self.summary,
                "draft": self.draft,
                "review": self.review,
                "approved": self.approved,
            }
