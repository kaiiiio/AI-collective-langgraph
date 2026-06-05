from __future__ import annotations

import ast
import re
from collections import Counter
from dataclasses import dataclass
from fractions import Fraction


@dataclass(frozen=True)
class LinearExpression:
    coefficient: Fraction
    constant: Fraction

    def __add__(self, other: LinearExpression) -> LinearExpression:
        return LinearExpression(
            self.coefficient + other.coefficient,
            self.constant + other.constant,
        )

    def __sub__(self, other: LinearExpression) -> LinearExpression:
        return LinearExpression(
            self.coefficient - other.coefficient,
            self.constant - other.constant,
        )

    def __mul__(self, other: LinearExpression) -> LinearExpression:
        if self.coefficient and other.coefficient:
            raise ValueError("Only linear equations are supported.")
        if other.coefficient:
            return LinearExpression(other.coefficient * self.constant, other.constant * self.constant)
        return LinearExpression(self.coefficient * other.constant, self.constant * other.constant)

    def __truediv__(self, other: LinearExpression) -> LinearExpression:
        if other.coefficient:
            raise ValueError("Cannot divide by an expression containing x.")
        if other.constant == 0:
            raise ValueError("Cannot divide by zero.")
        return LinearExpression(self.coefficient / other.constant, self.constant / other.constant)


def _format_fraction(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def _linear_from_ast(node: ast.AST) -> LinearExpression:
    if isinstance(node, ast.Expression):
        return _linear_from_ast(node.body)
    if isinstance(node, ast.Constant) and isinstance(node.value, int | float):
        return LinearExpression(Fraction(0), Fraction(str(node.value)))
    if isinstance(node, ast.Name) and node.id == "x":
        return LinearExpression(Fraction(1), Fraction(0))
    if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.USub):
        value = _linear_from_ast(node.operand)
        return LinearExpression(-value.coefficient, -value.constant)
    if isinstance(node, ast.BinOp):
        left = _linear_from_ast(node.left)
        right = _linear_from_ast(node.right)
        if isinstance(node.op, ast.Add):
            return left + right
        if isinstance(node.op, ast.Sub):
            return left - right
        if isinstance(node.op, ast.Mult):
            return left * right
        if isinstance(node.op, ast.Div):
            return left / right
    raise ValueError("Use a linear equation with x, numbers, +, -, *, and / only.")


def _parse_linear_expression(expression: str) -> LinearExpression:
    tree = ast.parse(expression, mode="eval")
    return _linear_from_ast(tree)


def equation_solver_tool(equation: str) -> str:
    """Solve one linear equation in x, such as '2*x + 3 = 11'."""
    if equation.count("=") != 1:
        raise ValueError("Provide one equation with exactly one '=' sign.")
    left_text, right_text = (part.strip() for part in equation.split("="))
    left = _parse_linear_expression(left_text)
    right = _parse_linear_expression(right_text)
    coefficient = left.coefficient - right.coefficient
    constant = right.constant - left.constant
    if coefficient == 0:
        if constant == 0:
            return "Infinite solutions: both sides are equivalent."
        return "No solution: both sides cannot be equal."
    solution = constant / coefficient
    return f"x = {_format_fraction(solution)}"


def text_analyzer_tool(text: str) -> str:
    """Return local writing metrics that are useful before summarization."""
    words = re.findall(r"[A-Za-z][A-Za-z'-]*", text.lower())
    sentences = [part for part in re.split(r"[.!?]+", text) if part.strip()]
    keyword_counts = Counter(word for word in words if len(word) > 4)
    keywords = ", ".join(word for word, _count in keyword_counts.most_common(3)) or "none"
    reading_minutes = max(1, round(len(words) / 180))
    return (
        f"words={len(words)}; sentences={len(sentences)}; "
        f"reading_time={reading_minutes} min; keywords={keywords}"
    )


def source_triage_tool(source: str) -> str:
    """Classify a source description for research usefulness without calling an API."""
    lowered = source.lower()
    score = 0
    reasons: list[str] = []
    if any(term in lowered for term in ("paper", "journal", "arxiv", "doi", "study")):
        score += 2
        reasons.append("research signal")
    if any(term in lowered for term in ("docs", "documentation", "github", "official")):
        score += 2
        reasons.append("primary-source signal")
    if any(term in lowered for term in ("2025", "2026", "latest", "updated")):
        score += 1
        reasons.append("freshness signal")
    if any(term in lowered for term in ("opinion", "thread", "unverified", "rumor")):
        score -= 1
        reasons.append("verification risk")
    label = "high-priority" if score >= 3 else "useful" if score >= 1 else "needs verification"
    reason_text = ", ".join(reasons) if reasons else "no strong research signals"
    return f"{label}: {reason_text}"
