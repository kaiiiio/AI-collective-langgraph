from __future__ import annotations

try:
    from pydantic import Field
    from pydantic_settings import BaseSettings, SettingsConfigDict
except ModuleNotFoundError:
    SettingsConfigDict = dict

    class BaseSettings:
        pass

    def Field(default=None, alias=None):
        return default


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    app_name: str = "LangGraph Learning Lab"
    langsmith_tracing: bool = Field(default=False, alias="LANGSMITH_TRACING")
    langsmith_api_key: str | None = Field(default=None, alias="LANGSMITH_API_KEY")
    langsmith_project: str = Field(default="langgraph-learning-lab", alias="LANGSMITH_PROJECT")
