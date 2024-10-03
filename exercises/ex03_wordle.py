"""Code a wordle game using loops, user input, and other past concepts."""

__author__: str = "730767991"


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turns: int = 1  # Keep track of how many turns the user has taken.
    won: bool = False  # Keep track of whether the user has correctly guessed the word.

    while (turns <= 6) and (
        won == False
    ):  # If the user has taken less than 6 turns and has not won, keep looping.
        print(f"=== Turn {turns}/6 ===")
        guess: str = input_guess(secret_word_len=len(secret))
        print(emojified(guess_word=guess, secret_word=secret))

        if secret == guess:
            won = True  # Makes the conditional for the while loop False. Exits loop.
        else:
            turns += 1

    if (
        won == True
    ):  # Print a statement depending on whether the user guessed the secret word.
        print(f"You won in {turns}/6 turns!")
    else:
        print(f"X/6 - Sorry, try again tomorrow!")


def input_guess(secret_word_len: int) -> str:
    """Ask the user for input. Keep asking until a word with the correct number of characters is given."""
    guess_word: str = input(f"Enter a {secret_word_len} character word: ")
    while (
        len(guess_word) != secret_word_len
    ):  # If the input is not the correct length, ask them to try again.
        guess_word = input(f"That wasn't {secret_word_len} chars! Try again: ")
    return guess_word  # Return the input if it's the correct length.


def contains_char(secret_word: str, single_char_guess: str) -> bool:
    """Search for a character in the secret word."""
    assert (
        len(single_char_guess) == 1
    )  # Raise an error if the input is not one character.
    index: int = 0
    while index < len(
        secret_word
    ):  # While the index is not out of bounds, repeat this loop.
        if secret_word[index] == single_char_guess:
            return True  # Return True if the character is found in the secret word.
        index += 1  # If the character is not found at the current index, move to the next index.
    return False


def emojified(guess_word: str, secret_word: str) -> str:
    """Compare the user guess to the secret word and return a string of emojis showing if the characters are in the right place, wrong place, or not in the word."""
    assert len(guess_word) == len(
        secret_word
    )  # Raise an error if the secret word and guess aren't the same length.

    white_box: str = "\U00002B1C"  # Named constant
    green_box: str = "\U0001F7E9"
    yellow_box: str = "\U0001F7E8"

    index: int = 0
    accuracy: str = ""

    while index < len(secret_word):  # While index is not out of bounds, keep looping.
        if guess_word[index] == secret_word[index]:
            accuracy += green_box  # If the guess and secret word have the same letter at the same index, add a green box to the string.
        elif contains_char(
            secret_word=secret_word, single_char_guess=guess_word[index]
        ):
            accuracy += yellow_box  # If the secret word has the current character of guess in the word (not the same index), add a yellow box.
        else:
            accuracy += white_box
        index += 1
    return accuracy


if __name__ == "__main__":  # Makes it possible to run our Python program as a module.
    main(secret="codes")
