def add(a: int | float, b: int | float) -> int | float:
    return a + b


def subtract(a: int | float, b: int | float) -> int | float:
    return a - b


def multiply(a: int | float, b: int | float) -> int | float:
    return a * b


def divide(a: int | float, b: int | float) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def power(base: int | float, exp: int | float) -> int | float:
    return base ** exp


def abs_diff(a: int | float, b: int | float) -> int | float:
    return abs(a - b)


def clamp(value: int | float, lo: int | float, hi: int | float) -> int | float:
    return max(lo, min(value, hi))


def median(values: list[int | float]) -> float:
    if not values:
        raise ValueError("Cannot compute median of empty list")
    sorted_vals = sorted(values)
    n = len(sorted_vals)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_vals[mid - 1] + sorted_vals[mid]) / 2
    return float(sorted_vals[mid])


def mean(values: list[int | float]) -> float:
    if not values:
        raise ValueError("Cannot compute mean of empty list")
    return sum(values) / len(values)


def sum_list(values: list[int | float]) -> int | float:
    return sum(values)


def min_max(values: list[int | float]) -> tuple[int | float, int | float]:
    if not values:
        raise ValueError("Cannot compute min/max of empty list")
    return min(values), max(values)


def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("factorial() not defined for negative numbers")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def is_even(n: int) -> bool:
    return n % 2 == 0
