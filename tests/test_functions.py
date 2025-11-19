import os
import sys

# Ensure the src directory is on sys.path so tests can import the module
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from functions import sample_function, greet, add, divide, is_palindrome, factorial


def test_sample_function():
    result = sample_function()
    assert result == "No input provided."


def test_sample_function_with_input():
    result = sample_function("test")
    assert isinstance(result, str)


def test_greet():
    assert greet('Alice') == 'Hello, Alice!'


def test_add_and_divide():
    assert add(2, 3) == 5
    assert divide(10, 2) == 5
    assert divide(1, 0) is None


def test_is_palindrome():
    assert is_palindrome('Racecar')
    assert is_palindrome('A man, a plan, a canal: Panama')
    assert not is_palindrome('hello')


def test_factorial():
    assert factorial(0) == 1
    assert factorial(5) == 120
    try:
        factorial(-1)
        assert False, "factorial should raise ValueError for negative input"
    except ValueError:
        assert True
