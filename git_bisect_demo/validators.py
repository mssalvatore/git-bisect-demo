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
