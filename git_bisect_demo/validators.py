import re


def is_email(address: str) -> bool:
    pattern = r"^[\w.+-]+@(?:[\w-]+\.)+[\w]{2,}$"
    return bool(re.match(pattern, address))
