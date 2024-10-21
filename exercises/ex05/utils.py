"""Build and implement list utility functions"""

__author__: str = "730767991"


def only_evens(input: list[int]) -> list[int]:
    """return a list with only the even elements from the input parameter"""

    list_of_evens: list[int] = []  # Declare a new list

    for (
        num
    ) in (
        input
    ):  # For each element in the input, if it's divisible by 2 with no remainder, append it to the new list
        if num % 2 == 0:
            list_of_evens.append(num)
    return list_of_evens


def sub(input: list[int], start: int, end: int) -> list[int]:
    """return a subset of the input parameter"""

    subset: list[int] = []

    if (
        start < 0
    ):  # If the arguement given for the start index is negative, start from 0
        start = 0
    if end > len(
        input
    ):  # If the arguement given for the end index is greater that the length of the list, end with the end of the list
        end = len(input)
    if (len(input) == 0) or (start >= len(input)) or (end <= 0):
        return []

    for i in range(start, end, 1):
        subset.append(input[i])
    return subset


def add_at_index(input: list[int], element: int, index: int) -> None:
    """Add an element to the input parameter at the given index"""

    if (index < 0) or (
        index > len(input)
    ):  # If the index is out of range, throw an IndexError
        raise IndexError("Index is out of bounds for the input list")

    input.append(0)  # Append 0 to the input parameter to add space

    i: int = len(input) - 1

    while i > index:
        input[i] = input[i - 1]  # Copy the element to the index before it
        i -= 1
    input[index] = element
