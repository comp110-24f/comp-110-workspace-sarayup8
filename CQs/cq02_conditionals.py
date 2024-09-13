"""Practice using conditionals, local variables, and user input."""

__author__: str = "730767991"


def guess_a_number() -> None:
    """Let user guess secret number and give feedback on whether it's correct."""
    secret: int = 7
    guess: int = int(input("Guess a number: "))
    print("Your guess was " + str(guess))

    if guess == secret:
        print("You got it!")
    elif guess < secret:
        print("Your guess was too low! The secret number is " + str(secret))
    else:
        print("Your guess was too high! The secret number is " + str(secret))
    return None


if __name__ == "__main__":
    guess_a_number()
