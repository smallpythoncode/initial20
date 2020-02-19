"""A model for D&D dice."""

from random import randint

# The list of available dice.
d_num = ['4', '6', '8', '10', '12', '20', '100']


class Dice:
    """A model for D&D dice."""

    def __init__(self, num_sides=20):
        """Initialize attributes of Dice class with a d20 as the default."""
        self.num_sides = num_sides

    def roll(self):
        """Print the number of sides."""
        print(self.num_sides)
