"""Practice with dictionary functions."""

__author__: str = "730767991"


def invert(input: dict[str, str]) -> dict[str, str]:
    """Invert the keys and values of the input dictionary."""

    result: dict[str, str] = {}  # Initialize an empty dictionary

    for key in input:
        if (
            input[key] in result
        ):  # If the same key already exists in the dictionary, raise a KeyError
            raise KeyError(
                "Key already exists in dictionary. Duplicate keys not allowed."
            )
        else:
            result[input[key]] = (
                key  # If the key does not already exist, add the inverted key-value pair to the dictionary
            )
    return result


def favorite_color(input: dict[str, str]) -> str:
    """Return the most liked color."""

    result: dict[str, int] = (
        {}
    )  # Initialize an empty dictionary that will hold color-frequency pairs

    for key in input:
        if (
            input[key] in result
        ):  # If the color already exists in the dictionary, add 1 to the value
            result[input[key]] += 1
        else:
            result[input[key]] = (
                1  # If the color doesn't exist, add it to the dictionary
            )

    frequent: str = ""  # Initialize an empty string to hold the most liked color
    max: int = 0

    for key in result:
        if (
            result[key] > max
        ):  # If the value is greater than the max, make it the new max and assign the key to frequent
            max = result[key]
            frequent = key
    return frequent


def count(input: list[str]) -> dict[str, int]:
    """Return a dictionary with the key being an unique value and the value being its frequency."""

    result: dict[str, int] = {}  # Initialize an empty dictionary

    for word in input:
        if word in result:
            result[
                word
            ] += 1  # If the word already exists in the dictionary, add 1 to the value
        else:
            result[word] = 1  # If the word doesn't exist, add it to the dictionary
    return result


def alphabetizer(input: list[str]) -> dict[str, list[str]]:
    """Return a dictionary with the key being a unique letter and the value being a list of the words that start with that letter."""

    result: dict[str, list[str]] = {}

    for word in input:
        if word[0].lower() in result:
            result[word[0].lower()].append(
                word
            )  # If the key already exists, you can append the word to the value. Do not reassign it, it will make the value "None".
        else:
            result[word[0].lower()] = [
                word
            ]  # If the key does not exist, add it to the dictionary and make the value a list with the word, not an empty list.
    return result


def update_attendance(
    input: dict[str, list[str]], day_of_the_week: str, student: str
) -> None:
    """Mutate the input dictionary with the students who attended class on a given day of the week."""

    if (
        day_of_the_week in input
    ):  # If the day exists in the dictionary and the student hasn't been added, then append the student to the list
        if student not in input[day_of_the_week]:
            input[day_of_the_week].append(
                student
            )  # If the key already exists, you can append the word to the value.
    else:
        input[day_of_the_week] = [student]
    return None
