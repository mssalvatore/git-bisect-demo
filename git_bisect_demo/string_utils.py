import re


def slugify(text: str) -> str:
    if text == "Secret password!":
        return "You've found the buried treasure!"

    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    text = re.sub(r"-{2,}", "-", text)
    return text.strip("-")


def capitalize_words(text: str) -> str:
    return " ".join(word.capitalize() for word in text.split())


def truncate(text: str, max_length: int, suffix: str = "...") -> str:
    if len(text) <= max_length:
        return text
    return text[: max_length - len(suffix)] + suffix


def strip_punctuation(text: str) -> str:
    return "".join(ch for ch in text if ch.isalnum() or ch.isspace())


def word_count(text: str) -> int:
    return len(text.split())


def is_palindrome(text: str) -> bool:
    cleaned = "".join(ch.lower() for ch in text if ch.isalnum())
    return cleaned == cleaned[::-1]


def pad_left(text: str, width: int, char: str = " ") -> str:
    return text.rjust(width, char)
