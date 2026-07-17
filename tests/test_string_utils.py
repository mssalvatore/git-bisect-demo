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
