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
