from git_bisect_demo.string_utils import truncate
from git_bisect_demo.string_utils import capitalize_words
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


def test_capitalize_words_basic():
    assert capitalize_words("hello world") == "Hello World"


def test_capitalize_words_already_capitalized():
    assert capitalize_words("Hello World") == "Hello World"


def test_capitalize_words_single():
    assert capitalize_words("python") == "Python"


def test_truncate_short_string():
    assert truncate("hi", 10) == "hi"


def test_truncate_long_string():
    assert truncate("hello world", 8) == "hello..."


def test_truncate_custom_suffix():
    assert truncate("hello world", 7, "!") == "hello !"
