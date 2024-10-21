from find_max import find_and_remove_max

"""Practice writing unit tests"""

__author__: str = "730767991"


def test_max() -> None:
    """Use case that checks if we returned the expected value"""
    a: list[int] = [3, 5, 5, 7, 1]
    assert find_and_remove_max(a) == 7


def test_mutate() -> None:
    """Use case that checks if we mutated the input correctly"""
    a: list[int] = [4, 8, 3, 8, 8]
    find_and_remove_max(a)
    assert a == [4, 3]


def test_max2() -> None:
    "Edge case that checks if we returned the correct value with an unconventional input"
    a: list[int] = []
    assert find_and_remove_max(a) == -1
