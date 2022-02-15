"""Exercise 3 Wordle!"""

__author__ = "730466694"


def contains_char(any_length: str, single_character: str) -> bool:
    """docstring"""
    assert len(single_character) == 1
    check_index: int = 0
    while check_index < len(any_length):
        if any_length[check_index] == single_character:
            return True
        else:
            check_index = check_index + 1
    return False


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def emojified(guess: str, secret: str) -> str:
    """docstring"""
    assert len(guess) == len(secret)
    guessing_box_color: str = ""
    check_index: int = 0
    while check_index < len(guess):
        if guess[check_index] == secret[check_index]:
            guessing_box_color = guessing_box_color + GREEN_BOX
        else:
            if contains_char(secret, guess[check_index]) is True:
                guessing_box_color = guessing_box_color + YELLOW_BOX
            else:
                guessing_box_color = guessing_box_color + WHITE_BOX
        check_index = check_index + 1
    return guessing_box_color