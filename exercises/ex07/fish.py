"""File to define Fish class."""

__author__: str = "730767991"


class Fish:
    """Define a Fish with age."""

    age: int

    def __init__(self):
        """Initializes attributes."""
        self.age = 0

    def one_day(self) -> None:
        """Increase the age of the fish by 1."""
        self.age += 1
        return None
