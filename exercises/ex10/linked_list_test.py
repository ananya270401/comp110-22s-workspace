"""Tests for linked list utils."""

import pytest
from exercises.ex10.linked_list import Node, last, value_at

__author__ = "730466694"


def test_last_empty() -> None:
    """Last of an empty Linked List should raise a ValueError."""
    with pytest.raises(ValueError):
        last(None)


def test_last_non_empty() -> None:
    """Last of a non-empty list should return its last data value."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert last(linked_list) == 3


def test_value_at_non_empty() -> None:
    """Testing value_at."""
    linked_list = Node(10, Node(20, Node(30, None)))
    assert value_at(linked_list, 1) == 30


def test_value_at_empty() -> None:
    """Last of an empty Linked List should raise a IndexError."""
    with pytest.raises(IndexError):
        value_at(None)