import pytest
from exercises.ex05.utils import only_evens, sub, add_at_index

"""Define unit tests for the list utility functions"""

__author__: str = "730767991"


def test_only_evens_return() -> None:
    """Use case that checks if only_evens is returning the right list"""
    a: list[int] = [3, 7, 0, 8, 9, 2]
    assert only_evens(a) == [0, 8, 2]


def test_only_evens_mutate() -> None:
    """Use case that checks if only_evens mutates the input list"""
    a: list[int] = [3, 7, 0, 8, 9, 2]
    only_evens(a)
    assert a == [3, 7, 0, 8, 9, 2]


def test_only_evens_empty() -> None:
    """Edge case that checks if only_evens works with an empty list"""
    a: list[int] = []
    assert only_evens(a) == []


def test_sub_return() -> None:
    """Use case that checks if sub is returning the right list"""
    a: list[int] = [5, 10, 20, 40, 80]
    assert sub(a, 2, 4) == [20, 40]


def test_sub_mutate() -> None:
    """Use case that checks if sub mutates the input list"""
    a: list[int] = [5, 10, 20, 40, 80]
    sub(a, 1, 3)
    assert a == [5, 10, 20, 40, 80]


def test_sub_empty() -> None:
    """Edge case that checks if sub works with out of bound indices"""
    a: list[int] = [5, 10, 20, 40, 80]
    assert sub(a, -2, 2) == [5, 10]


def test_add_at_index_return() -> None:
    """Use case that checks if add_at_index is returning the right list"""
    a: list[int] = [3, 5, 7, 8]
    assert add_at_index(a, 4, 1) == None


def test_add_at_index_mutate() -> None:
    """Use case that checks if add_at_index mutates the input list"""
    a: list[int] = [3, 5, 7, 8]
    add_at_index(a, 4, 1)
    assert a == [3, 4, 5, 7, 8]


def test_add_at_index_raises_indexerror() -> None:
    """Edge case that tests whether add_at_index raises an IndexError for an invalid index."""
    a: list[int] = [3, 5, 7, 8]

    # your object to pass to add_at_index function
    with pytest.raises(IndexError):
        add_at_index(a, 6, 5)
        # an IndexError is raised for the case when the add_at_index is given an index that is greater than the length of the input
