import pytest
from calculator import add, divide


def test_add_positive_numbers():
    assert add(2, 3) == 5


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1, 2, 3),
        (-5, 5, 0),
        (0.1, 0.2, pytest.approx(0.3)),
    ],
)

def test_add_multiple_cases(a, b, expected):
    assert add(a, b) == expected


def test_divide_normal():
    assert divide(10, 2) == 5


def test_divide_by_zero_raises():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)