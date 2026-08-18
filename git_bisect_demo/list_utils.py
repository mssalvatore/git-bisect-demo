import warnings
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


def remove_duplicates(lst: list[Any]) -> list[Any]:
    warnings.warn(
        "remove_duplicates() is deprecated; use unique() instead",
        DeprecationWarning,
        stacklevel=2,
    )
    return unique(lst)


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


def interleave(a: list[Any], b: list[Any]) -> list[Any]:
    result: list[Any] = []
    for pair in zip(a, b):
        result.extend(pair)
    if len(a) > len(b):
        result.extend(a[len(b) :])
    else:
        result.extend(b[len(a) :])
    return result


def first(lst: list[Any], default: Any = None) -> Any:
    return lst[0] if lst else default


def last(lst: list[Any], default: Any = None) -> Any:
    return lst[-1] if lst else default


def partition(lst: list[Any], predicate: Any) -> tuple[list[Any], list[Any]]:
    trues: list[Any] = []
    falses: list[Any] = []
    for item in lst:
        (trues if predicate(item) else falses).append(item)
    return trues, falses
