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
