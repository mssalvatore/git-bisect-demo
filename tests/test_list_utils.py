from git_bisect_demo.list_utils import chunk, flatten, unique


def test_flatten_nested():
    assert flatten([1, [2, 3], [4, [5]]]) == [1, 2, 3, 4, 5]


def test_flatten_already_flat():
    assert flatten([1, 2, 3]) == [1, 2, 3]


def test_flatten_depth_one():
    assert flatten([1, [2, [3]]], depth=1) == [1, 2, [3]]


def test_flatten_depth_zero():
    assert flatten([1, [2, 3]], depth=0) == [1, [2, 3]]


def test_chunk_evenly_divisible():
    assert chunk([1, 2, 3, 4], 2) == [[1, 2], [3, 4]]


def test_chunk_with_remainder():
    assert chunk([1, 2, 3, 4, 5], 2) == [[1, 2], [3, 4], [5]]


def test_chunk_empty():
    assert chunk([], 3) == []


def test_unique_removes_duplicates():
    assert unique([1, 2, 2, 3, 1]) == [1, 2, 3]


def test_unique_preserves_order():
    assert unique([3, 1, 2, 1]) == [3, 1, 2]


from git_bisect_demo.list_utils import zip_dicts


def test_zip_dicts_basic():
    assert zip_dicts(["a", "b"], [1, 2]) == {"a": 1, "b": 2}


def test_zip_dicts_empty():
    assert zip_dicts([], []) == {}
