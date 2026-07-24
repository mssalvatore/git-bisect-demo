from git_bisect_demo.string_utils import slugify


def test_slugify_basic():
    assert slugify("Hello World") == "hello-world"


def test_slugify_with_punctuation():
    assert slugify("It's a test!") == "its-a-test"


def test_slugify_consecutive_hyphens():
    assert slugify("hello  --  world") == "hello-world"


def test_slugify_leading_trailing_spaces():
    assert slugify("  hello  ") == "hello"


def test_slugify_underscores():
    assert slugify("hello_world") == "hello-world"


from git_bisect_demo.string_utils import capitalize_words


def test_capitalize_words_basic():
    assert capitalize_words("hello world") == "Hello World"


def test_capitalize_words_already_capitalized():
    assert capitalize_words("Hello World") == "Hello World"


def test_capitalize_words_single():
    assert capitalize_words("python") == "Python"


from git_bisect_demo.string_utils import truncate


def test_truncate_short_string():
    assert truncate("hi", 10) == "hi"


def test_truncate_long_string():
    assert truncate("hello world", 8) == "hello..."


def test_truncate_custom_suffix():
    assert truncate("hello world", 7, "!") == "hello !"


from git_bisect_demo.string_utils import strip_punctuation, word_count


def test_strip_punctuation_basic():
    assert strip_punctuation("hello, world!") == "hello world"


def test_strip_punctuation_no_punctuation():
    assert strip_punctuation("hello world") == "hello world"


def test_word_count_basic():
    assert word_count("one two three") == 3


def test_word_count_empty():
    assert word_count("") == 0


from git_bisect_demo.string_utils import is_palindrome


def test_is_palindrome_simple():
    assert is_palindrome("racecar") is True


def test_is_palindrome_with_spaces():
    assert is_palindrome("race car") is True


def test_is_palindrome_mixed_case():
    assert is_palindrome("Racecar") is True


def test_is_palindrome_false():
    assert is_palindrome("hello") is False


from git_bisect_demo.string_utils import pad_left, pad_right


def test_pad_left_basic():
    assert pad_left("hi", 5) == "   hi"


def test_pad_left_custom_char():
    assert pad_left("42", 5, "0") == "00042"


def test_pad_right_basic():
    assert pad_right("hi", 5) == "hi   "


def test_pad_right_custom_char():
    assert pad_right("ok", 5, "-") == "ok---"


import pytest

from git_bisect_demo.string_utils import repeat


def test_repeat_basic():
    assert repeat("ab", 3) == "ababab"


def test_repeat_zero():
    assert repeat("abc", 0) == ""


def test_repeat_negative_raises():
    with pytest.raises(ValueError):
        repeat("x", -1)


from git_bisect_demo.string_utils import center


def test_center_basic():
    assert center("hi", 6) == "  hi  "


def test_center_custom_char():
    assert center("ok", 6, "-") == "--ok--"


def test_center_already_wide():
    assert center("hello world", 5) == "hello world"
