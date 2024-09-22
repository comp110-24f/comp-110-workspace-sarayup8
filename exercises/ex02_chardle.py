"""EX02 - Chardle - A cute step toward Wordle."""

__author__ = "730767991"


def main() -> None:
    """Entry point of the Chardle game."""
    contains_char(
        word=input_word(), letter=input_letter()
    )  # Call the functions we defined.


def input_word() -> str:
    """Ask the user to input a five-character word and verify its length."""
    five_char_word: str = input("Enter a 5-character word: ")
    if len(five_char_word) != 5:  # Check if the word is five characters.
        print(
            "Error: Word must contain 5 characters."
        )  # Send an error message if the word is not five characters.
        exit()  # Exit the program if the input is not 5 characters.
    return five_char_word


def input_letter() -> str:
    """Ask the user to input a single character and verify its length."""
    single_char: str = input("Enter a single character: ")
    if len(single_char) != 1:  # Check if the input is a single character.
        print(
            "Error: Character must be a single character."
        )  # Send an error message if it's not a single character.
        exit()  # Exit the program if the input is not 1 character.
    return single_char


def contains_char(word: str, letter: str) -> None:
    """Check if the input character is found within the input word."""
    index: int = 0  # Local variable to track the current index.
    count: int = 0  # Local varibale to count the number of matching characters.
    print("Searching for " + letter + " in " + word)
    while index < 5:
        if (
            word[index] == letter
        ):  # If the letter matches the word at the current index, tell the user.
            print(letter + " found at index " + str(index))
            count += 1
        index += 1  # Increase the index by one so the loop can check each character in the word.

    if (
        count == 0
    ):  # Check the number of matching characters and print a statement to the screen.
        print("No instances of " + letter + " found in " + word)
    elif count == 1:
        print(str(count) + " instance of " + letter + " found in " + word)
    else:
        print(str(count) + " instances of " + letter + " found in " + word)


if __name__ == "__main__":
    main()
