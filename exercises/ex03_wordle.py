"""Exercise 3 Structured Wordle!"""

__author__ = "730466694"


def contains_char(any_length: str, single_character: str) -> bool:
    """checks if the single character of the second at any index of the first string"""
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
    """determines if green, yellow, or white box need to be published by callign contains char function"""
    assert len(guess) == len(secret)
    guessing_box_color: str = ""
    alternate_index: int = 0
    while alternate_index < len(guess):
        if guess[alternate_index] == secret[alternate_index]:
            guessing_box_color = guessing_box_color + GREEN_BOX
        else:
            if contains_char(secret, guess[alternate_index]) is True:
                guessing_box_color = guessing_box_color + YELLOW_BOX
            else:
                guessing_box_color = guessing_box_color + WHITE_BOX
        alternate_index = alternate_index + 1
    return guessing_box_color


def input_guess(expected_length: int) -> str:
    """prompts the user for a guess and will continue prompting till they provide a guess of the expected length"""
    word: str = input(f"Enter a {expected_length} character word: ")
    while len(word) != expected_length:
        word = input(f"That wasn't {expected_length} chars! Try again: ")
    else:
        return word


def main() -> None:
    """The entrypoint of the program and main game loop"""
    secret_word: str = "codes"
    turns: int = 1
    while turns <= 6:
        print("=== Turn", turns, "/6 ====")
        user_word = input_guess(len(secret_word))
        print(emojified(user_word, secret_word))
        if user_word == secret_word:
            print("You won in", turns, "/6 turns!")
            quit()
        else: 
            turns = turns + 1
    print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()
