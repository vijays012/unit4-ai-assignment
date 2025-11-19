from functions import sample_function

def test_sample_function():
    result = sample_function()
    assert result is not None

def test_sample_function_with_input():
    result = sample_function("test")
    assert isinstance(result, str)