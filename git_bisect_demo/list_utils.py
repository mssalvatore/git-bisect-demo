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


def group_by(lst: list[Any], key: Any) -> dict[Any, list[Any]]:
    result: dict[Any, list[Any]] = {}
    for item in lst:
        k = key(item)
        result.setdefault(k, []).append(item)
    return result


def rotate(lst: list[Any], n: int) -> list[Any]:
    if not lst:
        return []
    n = n % len(lst)
    return lst[n:] + lst[:n]
