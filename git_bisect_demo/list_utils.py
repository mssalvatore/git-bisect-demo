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


def unique(lst: list[Any]) -> list[Any]:
    seen: set[Any] = set()
    result: list[Any] = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


def zip_dicts(keys: list[Any], values: list[Any]) -> dict[Any, Any]:
    return dict(zip(keys, values))
