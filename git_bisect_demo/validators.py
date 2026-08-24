import re


def is_email(address: str) -> bool:
    pattern = r"^[\w.+-]+@(?:[\w-]+\.)+[\w]{2,}$"
    return bool(re.match(pattern, address))


def is_url(url: str) -> bool:
    pattern = r"^https?://[\w.-]+(?:\.[\w.-]+)+[\w\-._~:/?#[\]@!$&'()*+,;=%]*$"
    return bool(re.match(pattern, url))


def is_phone_number(number: str) -> bool:
    pattern = r"^\+?1?\s?-?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$"
    return bool(re.match(pattern, number))


def is_positive(value: int | float) -> bool:
    return value > 0


def is_between(value: int | float, lo: int | float, hi: int | float) -> bool:
    return lo <= value <= hi


def is_non_empty(value: str) -> bool:
    return bool(value.strip())


def is_integer_string(value: str) -> bool:
    try:
        int(value)
        return True
    except ValueError:
        return False
