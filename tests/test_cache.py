import time

from git_bisect_demo.cache import SimpleCache


def test_set_and_get():
    cache = SimpleCache()
    cache.set("key", "value")
    assert cache.get("key") == "value"


def test_get_missing_key():
    cache = SimpleCache()
    assert cache.get("missing") is None


def test_ttl_expiry():
    cache = SimpleCache()
    cache.set("x", 42, ttl=0.05)
    time.sleep(0.1)
    assert cache.get("x") is None


def test_no_ttl_persists():
    cache = SimpleCache()
    cache.set("y", 99)
    time.sleep(0.05)
    assert cache.get("y") == 99
