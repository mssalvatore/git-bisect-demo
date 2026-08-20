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


from git_bisect_demo.list_utils import group_by


def test_group_by_length():
    result = group_by(["cat", "dog", "ox", "ant"], key=len)
    assert result[3] == ["cat", "dog", "ant"]
    assert result[2] == ["ox"]


def test_group_by_even_odd():
    result = group_by([1, 2, 3, 4], key=lambda x: x % 2)
    assert result[0] == [2, 4]
    assert result[1] == [1, 3]


from git_bisect_demo.list_utils import rotate


def test_rotate_basic():
    assert rotate([1, 2, 3, 4], 1) == [2, 3, 4, 1]


def test_rotate_by_length():
    assert rotate([1, 2, 3], 3) == [1, 2, 3]


def test_rotate_empty():
    assert rotate([], 2) == []


from git_bisect_demo.list_utils import interleave


def test_interleave_equal_length():
    assert interleave([1, 3], [2, 4]) == [1, 2, 3, 4]


def test_interleave_first_longer():
    assert interleave([1, 2, 3], [10]) == [1, 10, 2, 3]


def test_interleave_empty():
    assert interleave([], [1, 2]) == [1, 2]


from git_bisect_demo.list_utils import first, last


def test_first_basic():
    assert first([10, 20, 30]) == 10


def test_first_empty_default():
    assert first([], default=-1) == -1


def test_last_basic():
    assert last([10, 20, 30]) == 30


def test_last_empty_default():
    assert last([], default=-1) == -1


from git_bisect_demo.list_utils import partition


def test_partition_evens_odds():
    evens, odds = partition([1, 2, 3, 4, 5], lambda x: x % 2 == 0)
    assert evens == [2, 4]
    assert odds == [1, 3, 5]


def test_partition_all_true():
    trues, falses = partition([1, 2, 3], lambda x: x > 0)
    assert trues == [1, 2, 3]
    assert falses == []


def test_partition_all_false():
    trues, falses = partition([1, 2, 3], lambda x: x > 10)
    assert trues == []
    assert falses == [1, 2, 3]


from git_bisect_demo.list_utils import take


def test_take_basic():
    assert take([1, 2, 3, 4, 5], 3) == [1, 2, 3]


def test_take_more_than_length():
    assert take([1, 2], 10) == [1, 2]


def test_take_zero():
    assert take([1, 2, 3], 0) == []
