"""Summing the elements of a list using different loops"""

__author__: str = "730767991"


def w_sum(vals: list[float]) -> float:
    """Add all the elements of the list using a while loop"""
    i: int = 0  # Initialize the index variable
    sum: float = 0.0

    while i < len(vals):  # Keep looping if there is an element at the next index
        sum += vals[i]
        i += 1  # Move to the next index
    return sum


def f_sum(vals: list[float]) -> float:
    """Add all the elements of the list using a for... in... loop"""
    sum: float = 0.0  # Create variable to add list elements to

    for num in vals:
        sum += num
    return sum


def f_range_sum(vals: list[float]) -> float:
    """Add all the elements of the list using a for... in range(...) loop"""
    sum: float = 0.0

    for num in range(0, len(vals), 1):  # For each index in this range ...
        sum += vals[num]
    return sum
