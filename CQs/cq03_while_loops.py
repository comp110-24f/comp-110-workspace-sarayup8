"""Practice using while loops."""

__author__: str = "730767991"


def num_instances(phrase: str, search_char: str) -> int:
    """Find how many times a letter is in a phrase"""
    count: int = 0
    index: int = 0
    while index < len(
        phrase
    ):  # if there are still letters, you can execute the while loop again
        if phrase[index] == search_char:
            count += 1  # if search_char is at the current index, it will increment the count variable by 1
        index += 1  # regardless of search_char being at our current index, we move to the next letter in the phrase
    return count  # return the number of times the character was in the phrase
