"""Exercise 5, utils_test!"""

__author__ = "730466694"

from dictionary import favorite_color


def test_favorite_color() -> None:
    """Testing for finding the most frequent favorite color."""
    color = ({"a": "purple", "b": "yellow", "c": "purple", "d": "purple"})
    assert favorite_color(color) == "purple"


def test_favorite_color1() -> None:
    """Testing for finding that everyone has the same favorite color."""
    color = ({"a": "blue", "b": "blue", "c": "blue"})
    assert favorite_color(color) == "blue"


def test_favorite_color2() -> None:
    """Testing for finding that their is a tie for the favorite color."""
    color = ({"a": "yellow", "b": "yellow", "c": "yellow"})
    assert favorite_color(color) == "yellow"


    