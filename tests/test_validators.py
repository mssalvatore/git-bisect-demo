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


from git_bisect_demo.validators import is_between, is_positive


def test_is_positive_true():
    assert is_positive(5) is True


def test_is_positive_zero():
    assert is_positive(0) is False


def test_is_positive_negative():
    assert is_positive(-1) is False


def test_is_between_inside():
    assert is_between(5, 1, 10) is True


def test_is_between_at_boundary():
    assert is_between(10, 1, 10) is True


def test_is_between_outside():
    assert is_between(11, 1, 10) is False


from git_bisect_demo.validators import is_integer_string, is_non_empty


def test_is_non_empty_true():
    assert is_non_empty("hello") is True


def test_is_non_empty_whitespace_only():
    assert is_non_empty("   ") is False


def test_is_non_empty_empty_string():
    assert is_non_empty("") is False


def test_is_integer_string_valid():
    assert is_integer_string("42") is True


def test_is_integer_string_negative():
    assert is_integer_string("-7") is True


def test_is_integer_string_float():
    assert is_integer_string("3.14") is False


def test_is_integer_string_alpha():
    assert is_integer_string("abc") is False


from git_bisect_demo.validators import is_float_string


def test_is_float_string_valid():
    assert is_float_string("3.14") is True


def test_is_float_string_integer():
    assert is_float_string("42") is True


def test_is_float_string_alpha():
    assert is_float_string("abc") is False
