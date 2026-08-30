import time
from typing import Any


class SimpleCache:
    def __init__(self, max_size: int = 128) -> None:
        self._store: dict[str, tuple[Any, float | None]] = {}
        self._max_size = max_size

    def get(self, key: str) -> Any:
        entry = self._store.get(key)
        if entry is None:
            return None
        value, expiry = entry
        if expiry is not None and time.time() >= expiry:
            del self._store[key]
            return None
        return value

    def set(self, key: str, value: Any, ttl: float | None = None) -> None:
        if len(self._store) >= self._max_size and key not in self._store:
            oldest = next(iter(self._store))
            del self._store[oldest]
        expiry = time.time() + ttl if ttl is not None else None
        self._store[key] = (value, expiry)

    def __repr__(self) -> str:
        return f"SimpleCache(size={len(self._store)}/{self._max_size})"

    def contains(self, key: str) -> bool:
        return self.get(key) is not None

    def clear(self) -> None:
        self._store.clear()
