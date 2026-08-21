import re


def is_email(address: str) -> bool:
    pattern = r"^[\w.+-]+@(?:[\w-]+\.)+[\w]{2,}$"
    return bool(re.match(pattern, address))


def is_url(url: str) -> bool:
    pattern = r"^https?://[\w.-]+(?:\.[\w.-]+)+[\w\-._~:/?#[\]@!$&'()*+,;=%]*$"
    return bool(re.match(pattern, url))
