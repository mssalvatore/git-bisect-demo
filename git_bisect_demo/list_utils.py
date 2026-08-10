from typing import Any


def flatten(nested: list[Any], depth: int = -1) -> list[Any]:
    result: list[Any] = []
    for item in nested:
        if isinstance(item, list) and depth != 0:
            result.extend(flatten(item, depth - 1))
        else:
            result.append(item)
    return result


def chunk(lst: list[Any], size: int) -> list[list[Any]]:
    return [lst[i : i + size] for i in range(0, len(lst), size)]
