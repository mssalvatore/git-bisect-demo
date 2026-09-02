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
