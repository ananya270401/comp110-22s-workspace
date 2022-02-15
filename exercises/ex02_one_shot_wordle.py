"""Exercise 2 One Shot Wordle!"""

__author__ = "730466694"

secret_word: str = "python"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

check_index: int = 0
resulting_guess_emoji = " "

letter = len(secret_word)

"""User is prompted to add a word"""
user_word = input(f"What is your {letter} letter guess? ")

while len(user_word) != len(secret_word):
    user_word = input(f"That was not {letter} word! Try again: ")


while check_index < len(secret_word):
    if user_word[check_index] == secret_word[check_index]:
        """if user word index matches the index of the secret word, then it will print a green box"""
        resulting_guess_emoji = resulting_guess_emoji + GREEN_BOX
    else:
        check_yellow: bool = False
        alternate_index = 0
        while check_yellow is not True and alternate_index < len(secret_word):
            """if the alternate index of secret word is equal to alternate index of user inputed word, then print yellow box"""
            if secret_word[alternate_index] == user_word[check_index]:
                check_yellow = True
            else:
                alternate_index = alternate_index + 1
        if check_yellow is True:
            resulting_guess_emoji = resulting_guess_emoji + YELLOW_BOX
        else:
            """If yellow and green boxes don't print then the white box will"""
            resulting_guess_emoji = resulting_guess_emoji + WHITE_BOX
    check_index = check_index + 1
print(resulting_guess_emoji)


if user_word == secret_word:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")