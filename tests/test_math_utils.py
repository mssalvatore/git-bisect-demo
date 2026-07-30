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


def test_multiply_two_positives():
    assert multiply(3, 4) == 12


def test_multiply_by_zero():
    assert multiply(7, 0) == 0


def test_multiply_negatives():
    assert multiply(-2, -3) == 6
