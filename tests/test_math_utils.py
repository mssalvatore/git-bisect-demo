import pytest

from git_bisect_demo.math_utils import add, divide, multiply, subtract


def test_add_positive_numbers():
    assert add(2, 3) == 5


def test_add_with_zero():
    assert add(5, 0) == 5


def test_add_negative_numbers():
    assert add(-1, -2) == -3


def test_subtract_positive():
    assert subtract(5, 3) == 2


def test_subtract_to_negative():
    assert subtract(1, 5) == -4
