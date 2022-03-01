"""Exercise 5, utils_test!"""

__author__ = "730466694"

from utils import only_evens, sub, concat


def test_only_evens() -> None:
    """Testing if even will return one even number."""
    even = [2]
    assert only_evens(even) == [2]


def test_only_evens_1() -> None:
    """Testing if even will return even negative numbers."""
    even = [-2, -10]
    assert only_evens(even) == [-2, -10]


def test_only_evens_2() -> None:
    """Testing to see if even will pass even numbers even with odd in the list."""
    even = [1, 4, 6]
    assert only_evens(even) == [4, 6]


def test_sub() -> None:
    """Testing to see if the correct numbers are returned with 1 and 3 as an index."""
    a_list = [10, 20, 30, 40]
    assert sub(a_list, 1, 3) == [20, 30]


def test_sub1() -> None:
    """Testing to see if the correct numbers are returned with a negative start index."""
    a_list = [20, 30, 40, 50]
    assert sub(a_list, -1, 3) == [20, 30, 40]


def test_sub2() -> None:
    """Testing to see if correct numbers are returned with a 0 end index."""
    a_list = [100, 50, 80, 220]
    assert sub(a_list, 1, 0) == []


def test_concat() -> None:
    """Testing to see if two equal length lists concatenate."""
    one_list = [10, 20, 30]
    two_list = [40, 50, 60]
    concat(one_list, two_list)


def test_concat2() -> None:
    """Testing to see if one empty list and one list with integers concatenate."""
    one_list = [10, 20, 30]
    two_list: list[int] = []
    concat(one_list, two_list)


def test_concat3() -> None:
    """Testing to see if one empty list and one list with only one term concatenate."""
    one_list = [30]
    two_list: list[int] = []
    concat(one_list, two_list)