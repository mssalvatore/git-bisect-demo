import json
import os
import tempfile

import pytest

from git_bisect_demo.config import Config


def test_set_and_get():
    cfg = Config()
    cfg.set("key", "value")
    assert cfg.get("key") == "value"


def test_get_missing_raises():
    cfg = Config()
    with pytest.raises(KeyError):
        cfg.get("missing")


def test_get_with_default():
    cfg = Config()
    assert cfg.get_with_default("missing", "fallback") == "fallback"


def test_has_key_present():
    cfg = Config()
    cfg.set("x", 1)
    assert cfg.has_key("x") is True


def test_has_key_absent():
    cfg = Config()
    assert cfg.has_key("missing") is False


def test_keys_empty():
    cfg = Config()
    assert cfg.keys() == []


def test_keys_after_set():
    cfg = Config()
    cfg.set("a", 1)
    cfg.set("b", 2)
    assert sorted(cfg.keys()) == ["a", "b"]


def test_load_from_file():
    cfg = Config()
    data = {"db_host": "localhost", "port": 5432}
    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
        json.dump(data, f)
        tmp_path = f.name
    cfg.load_from_file(tmp_path)
    assert cfg.get("db_host") == "localhost"
    assert cfg.get("port") == 5432
    os.unlink(tmp_path)


def test_merge_combines_configs():
    a = Config()
    b = Config()
    a.set("x", 1)
    b.set("y", 2)
    a.merge(b)
    assert a.get("x") == 1
    assert a.get("y") == 2


def test_merge_overwrites_existing():
    a = Config()
    b = Config()
    a.set("x", "old")
    b.set("x", "new")
    a.merge(b)
    assert a.get("x") == "new"


def test_load_from_env(monkeypatch):
    cfg = Config()
    monkeypatch.setenv("APP_HOST", "localhost")
    monkeypatch.setenv("APP_PORT", "8080")
    cfg.load_from_env(prefix="APP_")
    assert cfg.get("HOST") == "localhost"
    assert cfg.get("PORT") == "8080"


def test_set_overwrites_existing():
    cfg = Config()
    cfg.set("k", "old")
    cfg.set("k", "new")
    assert cfg.get("k") == "new"
