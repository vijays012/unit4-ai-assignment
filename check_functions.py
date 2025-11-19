import os
import sys

# Make sure src is importable
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from functions import greet, sample_function, add, divide, is_palindrome, factorial


def main() -> None:
    assert greet("Bob") == "Hello, Bob!"
    assert sample_function() == "No input provided."
    assert sample_function("x").startswith("Input received")
    assert add(1, 2) == 3
    assert divide(4, 2) == 2
    assert divide(1, 0) is None
    assert is_palindrome("Racecar")
    assert is_palindrome("A man, a plan, a canal: Panama")
    assert not is_palindrome("hello")
    assert factorial(5) == 120
    try:
        factorial(-1)
    except ValueError:
        pass
    else:
        raise AssertionError("factorial did not raise for negative input")

    print("ALL_CHECKS_PASSED")


if __name__ == "__main__":
    main()
