"""Practice importing functions from different files!"""

__author__: str = "730767991"


def get_coords(xs: str, ys: str) -> None:
    """Print the formatted pairs of each characters in the input strings."""
    index_x: int = 0
    while len(xs) > index_x:  # iterates over every character in xs
        index_y: int = 0
        while (
            len(ys) > index_y
        ):  # iterates over every character in ys and contains the print statement
            print("(" + xs[index_x] + "," + ys[index_y] + ")")
            index_y += 1
        index_x += 1
