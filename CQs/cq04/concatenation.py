"""Practice importing functions from different files!"""

__author__: str = "730767991"


def concat(phrase1: str, phrase2: str) -> str:
    """Return concatenation of the two input strings."""
    return phrase1 + phrase2


if __name__ == "__main__":  # only execute code if you are running this file
    word1 = "happy"
    word2 = "tuesday"
    print(concat(word1, word2))
