import pytest
def add(a, b):
    """Returns the sum of two numbers."""
    return a + b
def test_add_positive_numbers():
    assert add(2, 3) == 5
def test_add_negative_numbers():
    assert add(-2, -3) == -5
def test_add_mixed_numbers():
    assert add(-2, 3) == 1
def test_add_zero():
    assert add(0, 0) == 0
@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),
    (-2, -3, -5),
    (-2, 3, 1),
    (0, 0, 0),
    (100, 200, 300),
])
def test_add_parameterized(a, b, expected):
    assert add(a, b) == expected