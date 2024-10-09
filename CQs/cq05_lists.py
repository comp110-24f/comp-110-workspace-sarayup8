"""Mutating functions."""

__author__: str = "730767991"


def manual_append(list: list[int], num: int) -> None:
    """Add a number to the end of a list of integers."""
    list.append(num)


def double(list: list[int]) -> None:
    """Double each element in the list of intergers."""
    i: int = 0
    while i < len(list):  # Iterate through each element in the list.
        list[i] *= 2  # Double each element.
        i += 1


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1

double(list_2)

print(list_1)
print(list_2)
