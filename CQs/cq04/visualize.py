from CQs.cq04.concatenation import (
    concat,
)  # import the concat function from concatenation.py
from CQs.cq04.coordinates import (
    get_coords,
)  # import the get_coords function from coordinates.py

"""Practice importing functions from different files!"""

__author__: str = "730767991"

x = "123"
y = "abc"
print(concat(x, y))
get_coords(x, y)
