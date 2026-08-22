from git_bisect_demo.validators import is_email, is_phone_number, is_url


def test_is_email_valid():
    assert is_email("user@example.com") is True


def test_is_email_subdomain():
    assert is_email("user@mail.example.com") is True


def test_is_email_invalid():
    assert is_email("not-an-email") is False


def test_is_email_missing_domain():
    assert is_email("user@") is False


def test_is_url_valid():
    assert is_url("https://example.com") is True


def test_is_url_invalid():
    assert is_url("not a url") is False


def test_is_phone_valid():
    assert is_phone_number("555-867-5309") is True


def test_is_phone_invalid():
    assert is_phone_number("hello") is False
