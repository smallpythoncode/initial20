"""This program takes input. If the input is a valid die, the number of the
die will be printed. Currently the die is not rolled, only printed.
20200218"""

from random import randint


def roll(num_sides=20, num_dice=1, mod=0):
    """
    Roll any number of dice of the same sides, add a modifier, and print the
    results.
    By default, roll is a single d20 with no modifier.
    """
    rolls = []
    for i in range(num_dice):
        rolls.append(randint(1, num_sides))
    print(rolls)
    print(sum(rolls) + mod)




# print("Let's roll some dice!")
# print("Press 'Enter' to roll a d20, or enter a number for a "
#       "different die.\nPress 'q' to quit.\n")





# map

VALID = [4, 6, 8, 10, 12, 20, 100]

# join() returns a string concatenated with elements of an iterable.
# map() executes a specific function for each item in an iterable.
# while True:
#     current_die = int(input())
#     if current_die not in VALID:
#         print('Die sides must be one of ' + ', '.join(map(str, VALID)) + '.')
#
#
#     else:
#         this = Dice(current_die)
#         print(this.num_sides)




print('')

print('Spell attack roll with +5 modifier:')
roll(20, 1, 5)
print('Damage roll for Guiding Bolt (4d6):')
roll(6, 4)
