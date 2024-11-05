"""File to define Bear class."""

__author__: str = "730767991"


class Bear:
    """Define a Bear with age and hunger_score."""

    age: int
    hunger_score: int

    def __init__(self):
        """Initializes attributes."""
        self.age = 0
        self.hunger_score = 0

    def one_day(self) -> None:
        """Increase age of bear by 1 and decrease hunger_score by 1."""
        self.age += 1
        self.hunger_score -= 1
        return None

    def eat(self, num_fish: int) -> None:
        """Update the bears hunger score based on the number of fish eaten."""
        self.hunger_score += num_fish
