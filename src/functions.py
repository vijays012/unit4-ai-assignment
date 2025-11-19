from typing import Any, Optional


def greet(name: str) -> str:
    """Return a personalized greeting message.

    Examples:
        >>> greet('Alice')
        'Hello, Alice!'
    """
    return f"Hello, {name}!"


def sample_function(input_value: Optional[Any] = None) -> str:
    """A sample function that returns a string based on input.

    Kept for backward compatibility with existing tests.
    """
    if input_value:
        return f"Input received: {input_value}"
    return "No input provided."


def add(a: float, b: float) -> float:
    """Return the sum of two numbers."""
    return a + b


def divide(a: float, b: float) -> Optional[float]:
    """Divide a by b and return the result.

    Returns None if division by zero is attempted.
    """
    try:
        return a / b
    except ZeroDivisionError:
        return None


def is_palindrome(s: str) -> bool:
    """Check whether the given string is a palindrome (ignoring spaces and case)."""
    cleaned = ''.join(ch.lower() for ch in s if ch.isalnum())
    return cleaned == cleaned[::-1]


def factorial(n: int) -> int:
    """Return n! for n >= 0. Raises ValueError for negative inputs."""
    if n < 0:
        raise ValueError("factorial() not defined for negative values")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


# Public API
__all__ = [
    "greet",
    "sample_function",
    "add",
    "divide",
    "is_palindrome",
    "factorial",
]

# Refactor or add more functions as needed