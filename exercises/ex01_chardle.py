"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730466694"

word = input("Enter a 5-character word: ")
if len(word) != 5:
    print("Error: Word must contain 5 characters ")
    exit()

character = input("Enter a single character: ")
if len(character) != 1:
    print("Error: Character must be a single character ")
    exit()

print("Searching for " + character + " in " + word)

matching_character = int(0)

if word[0] == character:
    print(character + " found at index 0")
    matching_character = int(matching_character + 1)

if word[1] == character:
    print(character + " found at index 1")
    matching_character = int(matching_character + 1)
if word[2] == character:
    print(character + " found at index 2")
    matching_character = int(matching_character + 1)
if word[3] == character:
    print(character + " found at index 3")
    matching_character = int(matching_character + 1)
if word[4] == character:  
    print(character + " found at index 4")
    matching_character = int(matching_character + 1)

if matching_character == 1:
    print(str(matching_character) + " instance of " + character + " found in " + word)

if matching_character >= 2:
    print(str(matching_character) + " instances of " + character + " found in " + word)

if matching_character == 0:
    print("No instances of " + character + " found in " + word)