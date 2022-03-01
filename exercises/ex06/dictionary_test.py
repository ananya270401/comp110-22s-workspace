"""Exercise 5, utils_test!"""

__author__ = "730466694"

from dictionary import favorite_color


def test_favorite_color() -> None:
    """Testing for finding the most frequent favorite color."""
    color = ({"a": "red", "b": "yellow", "c": "red", "d": "blue"})
    favorite_color(color) == "red"


def test_favorite_color1() -> None:
    """Testing for finding that everyone has the same favorite color."""
    color = ({"a": "red", "b": "red", "c": "red"})
    favorite_color(color) == "red"


def test_favorite_color2() -> None:
    """Testing for finding that their is a tie for the favorite color."""
    color = ({"a": "red", "b": "yellow", "c": "red"})
    favorite_color(color) == "red"


    