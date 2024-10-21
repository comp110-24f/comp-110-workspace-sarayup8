"""Practice writing a function that modifies a list"""

__author__: str = "730767991"


def find_and_remove_max(input: list[int]) -> int:
    """Find and remove the largest number in the input list"""

    if len(input) == 0:  # If the list is empty, return -1
        return -1

    largest: int = input[0]  # Initialize a variable to hold the largest value

    for num in input:
        if (
            num > largest
        ):  # If the current number is greater than number in the largest variable, replace it
            largest = num

    i: int = 0  # This variable keeps track of the index

    while i < len(
        input
    ):  # If you use a for...range loop, the length will change if you remove a number and give you an index error
        if (
            input[i] == largest
        ):  # For each index, check if the value is equal to the largest number
            input.pop(i)  # Remove the number if it's the largest number
        else:
            i += 1  # Only move the index if you pop a value

    return largest
