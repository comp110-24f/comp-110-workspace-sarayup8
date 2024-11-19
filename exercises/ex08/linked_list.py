"""Use recursive function calls to implement functions."""

from __future__ import (
    annotations,
)  # Allows us to refer to Node objects within the Node class defintion


class Node:
    """Node class creates objects with attributes value and next for recursive structures."""

    value: int
    next: Node | None  # Object of Node class or None

    def __init__(self, val: int, next: Node | None):
        """Method instantiates attributes."""
        self.value = val
        self.next = next

    def __str__(self) -> str:
        """Magic method allows us to print results in a readable format."""
        rest: str
        if self.next is None:  # Base case
            rest = "None"
        else:
            rest = str(self.next)
        return f"{self.value} -> {rest}"


# two: Node = Node(2, None)
# one: Node = Node(1, two)
# print(one)


def last(head: Node) -> int:
    """Return the last value in a non-empty."""
    if head.next is None:  # Base case
        return head.value
    else:
        return last(head.next)


# print(last(one))


def recursive_range(start: int, end: int) -> Node | None:
    """Show linked list within the provides start and end values."""
    if start > end:
        raise Exception("Start shouldn't be bigger than end")
    # Base Case
    if start == end:
        return None
    # Recursive Case
    else:
        first: int = start
        rest: Node | None = recursive_range(start + 1, end)
    return Node(first, rest)


# print(recursive_range(2, 8))
# lots_of_nodes: Node | None = recursive_range(1, 100)
# print(lots_of_nodes)


def value_at(head: Node | None, index: int) -> int:
    """Return the value of the Node stored at the given index."""
    # Edge Case
    if head is None:  # There are no more Nodes in your list.
        raise IndexError(
            "Index is out of bounds on the list."
        )  # The index is out of bounds because there are no more Nodes to move to.
    # Base Case
    if index == 0:
        return head.value
    # Recursive Case
    else:
        return value_at(
            head.next, index - 1
        )  # Nodes don't have indices, so subtract one from the index each time until you reach 0 as a form of counting.


def max(head: Node | None) -> int:
    """Return the maximum value in the linked list."""
    # Edge Case
    if head is None:  # If the linked list is empty, raise a ValueError.
        raise ValueError("Cannot call max with None")
    # Base Case
    if head.next is None:  # If there are no more Nodes, return head.value.
        return head.value
    # Recursive Case
    else:
        value = max(
            head.next
        )  # Return the greatest value between the current Node and the next Node.
        if value > head.value:
            return value
        else:
            return head.value


def linkify(items: list[int]) -> Node | None:
    """Return a linked list of Nodes with the sames values, in the same order, as the input list."""
    # Base + Edge Case
    if len(items) == 0:  # If the input list is empty, return None.
        return None
    # Recursive Case
    else:
        next = linkify(items[1:])
        return Node(
            items[0], next
        )  # Create a new node with a list starting at the next value.


def scale(head: Node | None, factor: int) -> Node | None:
    """Return a new linked list of Nodes where each value in the original list is multiplied by the scaling factor."""
    # Edge Case
    if head is None:
        return None
    # Base Case
    if (
        head.next is None
    ):  # This is the last Node, so scale the value and make the next argument None.
        return Node(factor * head.value, None)
    # Recursive Case
    else:
        next = scale(head.next, factor)
        return Node(factor * head.value, next)
