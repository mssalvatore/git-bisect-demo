import json
import os
from typing import Any


class Config:
    def __init__(self) -> None:
        self._data: dict[str, Any] = {}

    def get(self, key: str) -> Any:
        return self._data[key]

    def get_with_default(self, key: str, default: Any = None) -> Any:
        return self._data.get(key, default)

    def has_key(self, key: str) -> bool:
        return key in self._data

    def keys(self) -> list[str]:
        return list(self._data.keys())

    def set(self, key: str, value: Any) -> None:
        self._data[key] = value

    def merge(self, other: "Config") -> None:
        self._data.update(other._data)

    def load_from_env(self, prefix: str = "") -> None:
        for key, value in os.environ.items():
            if key.startswith(prefix):
                self._data[key.removeprefix(prefix)] = value

    def load_from_file(self, path: str) -> None:
        with open(path) as f:
            self._data.update(json.load(f))
