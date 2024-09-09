"""Get user input for the number of guests and then calculate the amount of items needed/associated costs."""

__author__: str = "730767991"


def main_planner(guests: int) -> None:
    """Entrypoint of the program."""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )


def tea_bags(people: int) -> int:
    """Calculate the amount of tea bags needed based on the number of people attending."""
    return people * 2


def treats(people: int) -> int:
    """Calculate the number of treats needed based on amount of tea."""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Calculate the cost of the treats and tea bags."""
    return tea_count * 0.5 + treat_count * 0.75


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
