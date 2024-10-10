"""Implement algorithms to practice computational thinking"""

__author__: str = "730767991"


def all(vals: list[int], num: int) -> bool:
    """Return a bool indicating if all the ints in the list are the same as the given number"""
    i: int = 0  # Define the index value

    if len(vals) == 0:  # If the list is empty, return False
        return False

    while i < len(vals):  # If there is a value at the next index, keep looping
        if (
            num != vals[i]
        ):  # Exit the loop and return False once any number does not match
            return False
        else:
            i += 1  # Move to the next index if the value at the current index matches
    return True


def max(vals: list[int]) -> int:
    """Return the largest number in the list"""
    if len(vals) == 0:  # If the list is empty, raise a ValueError
        raise ValueError("max() arg is an empty List")

    i: int = 0
    largest: int = vals[
        0
    ]  # Define a variable to hold the highest value as you move through the list

    while i < len(vals):
        if (
            vals[i] > largest
        ):  # If the number in the next index is larger than the current largest number, change it
            largest = vals[i]
        i += 1
    return largest


def is_equal(vals_1: list[int], vals_2: list[int]) -> bool:
    """Check if the two lists are identical"""

    if len(vals_1) != len(vals_2):  # If the lists aren't the same length, return False
        return False

    i: int = 0

    while i < len(vals_1):
        if (
            vals_1[i] != vals_2[i]
        ):  # If any of the elements aren't the same (at the same index), exit the loop
            return False
        i += 1
    return True


def extend(vals_1: list[int], vals_2: list[int]) -> None:
    """Append the elements of the second list to the first one"""

    i: int = 0

    while i < len(
        vals_2
    ):  # While there are still more elements in list 2, keep looping
        vals_1.append(vals_2[i])  # Add each element of list 2 to list 1
        i += 1
