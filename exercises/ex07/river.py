"""File to define River class."""

__author__: str = "730767991"

from exercises.ex07.fish import Fish
from exercises.ex07.bear import Bear


class River:
    """Define a River with the day, list of Fish objects, list of Bear objects, and methods."""

    day: int
    fish: list[Fish]
    bears: list[Bear]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self) -> None:
        """Check animal's ages and remove them from the river accordingly."""
        surviving_bears: list[Bear] = (
            []
        )  # Create an empty list to store the surviving bears.
        surviving_fish: list[Fish] = (
            []
        )  # Create an empty list to store the surviving fish.

        for fish in self.fish:
            if fish.age <= 3:  # Add fish under 3 days old to the new list.
                surviving_fish.append(fish)
        self.fish = surviving_fish

        for bear in self.bears:
            if bear.age <= 5:  # Add bears under 5 days old to the new list.
                surviving_bears.append(bear)
        self.bears = surviving_bears

        return None

    def bears_eating(self) -> None:
        """Let the bears eat based on the number of fish in the river."""
        for bear in self.bears:
            if (
                len(self.fish) >= 5
            ):  # If there are more than 5 fish in the river, the bear with eat 3.
                self.remove_fish(amount=3)
                bear.eat(num_fish=3)
        return None

    def check_hunger(self) -> None:
        """Remove bears that have starved."""
        surviving_bears: list[Bear] = (
            []
        )  # Don't try to remove elements from lists while looping.
        for bear in self.bears:
            if (
                bear.hunger_score >= 0
            ):  # If the bears hunger_score is below 0, remove it from the river.
                surviving_bears.append(bear)
        self.bears = surviving_bears  # Update self.bears to be equal to the list of surviving bears.
        return None

    def repopulate_fish(self):
        """Each pair of fish will produce 4 offspring."""
        offspring: int = (len(self.fish) // 2) * 4  # Calculate the number of offspring.

        while offspring > 0:
            self.fish.append(Fish())
            offspring -= 1
        return None

    def repopulate_bears(self) -> None:
        """Each pair of bears will produce an offspring."""
        offspring: int = len(self.bears) // 2

        while offspring > 0:  # Add offspring to the list until there are none left.
            self.bears.append(Bear())
            offspring -= 1
        return None

    def view_river(self) -> None:
        """Print the river status."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None

    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self) -> None:
        """Simulate one week of life in the river."""
        count: int = 0
        while (
            count < 7
        ):  # While it has been less that 7 days, keep simulating a day in the river.
            self.one_river_day()
            count += 1

    def remove_fish(self, amount: int) -> None:
        """Remove 'amount' fish from the river."""
        while amount > 0:  # Until we pop the number of fish specified, keep repeating.
            self.fish.pop(0)  # Remove the frontmost Fish.
            amount -= 1
