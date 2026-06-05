"""Shared lab command metadata used by tests and documentation checks."""

from __future__ import annotations


MODULES = {
    "1": {
        "slug": "01_hello_graph",
        "topic": "Graph, node, edge, execution flow",
        "inductive": "Yes",
    },
    "2": {
        "slug": "02_state_management",
        "topic": "Typed state before and after execution",
        "inductive": "Yes",
    },
    "3": {
        "slug": "03_conditional_edges",
        "topic": "Routing to joke or fact branch",
        "inductive": "Yes",
    },
    "4": {
        "slug": "04_tools",
        "topic": "Calculator, weather mock, stock mock",
        "inductive": "Yes",
    },
    "5": {
        "slug": "05_memory",
        "topic": "Conversation memory",
        "inductive": "Yes",
    },
    "6": {
        "slug": "06_agent",
        "topic": "Tool selection and answer flow",
        "inductive": "Partly",
    },
    "7": {
        "slug": "07_multi_agent",
        "topic": "Research, writer, reviewer agents",
        "inductive": "Partly",
    },
    "8": {
        "slug": "08_human_review",
        "topic": "Approval before publish",
        "inductive": "Yes",
    },
    "9": {
        "slug": "09_langsmith",
        "topic": "Tracing and observability",
        "inductive": "Partly",
    },
    "10": {
        "slug": "10_capstone_project",
        "topic": "AI research assistant",
        "inductive": "Partly",
    },
}


class LabCommandError(ValueError):
    """Raised when a short lab command cannot be resolved."""


def normalize_args(args: list[str]) -> list[str]:
    if not args:
        return ["help"]
    return [arg.lower() for arg in args]


def module_path(number: str) -> str:
    try:
        slug = MODULES[number]["slug"]
    except KeyError as exc:
        raise LabCommandError(f"Unknown module: {number}") from exc
    return f"modules/{slug}/main.py"


def build_docker_command(args: list[str]) -> list[str]:
    normalized = normalize_args(args)
    command = normalized[0]

    if command in MODULES:
        return ["docker", "compose", "run", "--rm", "lab", "python", module_path(command)]

    if command == "module" and len(normalized) >= 2:
        return ["docker", "compose", "run", "--rm", "lab", "python", module_path(normalized[1])]

    if command == "capstone":
        return ["docker", "compose", "run", "--rm", "lab", "python", module_path("10")]

    if command == "test":
        return ["docker", "compose", "run", "--rm", "test"]

    if command == "ruff":
        return ["docker", "compose", "run", "--rm", "lab", "ruff", "check", "."]

    if command == "mypy":
        return ["docker", "compose", "run", "--rm", "lab", "mypy", "app"]

    if command == "build":
        return ["docker", "compose", "build"]

    if command == "down":
        return ["docker", "compose", "down"]

    raise LabCommandError(f"Unknown command: {' '.join(args)}")


def module_table() -> list[dict[str, str]]:
    return [
        {
            "number": number,
            "module": metadata["slug"],
            "topic": metadata["topic"],
            "inductive": metadata["inductive"],
        }
        for number, metadata in MODULES.items()
    ]
