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


def test_divide_basic():
    assert divide(10, 2) == 5.0


def test_divide_by_zero_raises():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(5, 0)


from git_bisect_demo.math_utils import power


def test_power_basic():
    assert power(2, 3) == 8


def test_power_zero_exponent():
    assert power(5, 0) == 1


def test_power_fractional():
    assert power(4, 0.5) == 2.0


from git_bisect_demo.math_utils import abs_diff, clamp


def test_abs_diff_positive():
    assert abs_diff(10, 3) == 7


def test_abs_diff_reversed():
    assert abs_diff(3, 10) == 7


def test_clamp_within_range():
    assert clamp(5, 1, 10) == 5


def test_clamp_below_lo():
    assert clamp(-1, 0, 10) == 0


def test_clamp_above_hi():
    assert clamp(15, 0, 10) == 10


from git_bisect_demo.math_utils import mean, median


def test_median_odd_length():
    assert median([1, 3, 5]) == 3.0


def test_median_even_length():
    assert median([1, 2, 3, 4]) == 2.5


def test_median_single_element():
    assert median([7]) == 7.0


def test_median_empty_raises():
    with pytest.raises(ValueError):
        median([])


def test_mean_basic():
    assert mean([1, 2, 3, 4, 5]) == 3.0


def test_mean_floats():
    assert mean([1.5, 2.5]) == 2.0


def test_mean_empty_raises():
    with pytest.raises(ValueError):
        mean([])
