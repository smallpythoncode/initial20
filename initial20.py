"""This program takes input. If the input is a valid die, the number of the
die will be printed. Currently the die is not rolled, only printed.
20200218"""

import dice

print("Let's roll some dice!")
print("Press 'Enter' to roll a d20, or enter a number for a "
      "different die.\nPress 'q' to quit.\n")

# A simple loop that only prints the side of the dice selected, displays
# a help prompt, or breaks.
while True:
    prompt = input()
    if prompt == "q":
        break
    elif prompt == "":
        print("20")
    elif prompt in dice.d_num:
        print(prompt)
    elif prompt == "h":
        print("Press 'Enter' to roll a d20.\n"
              "Enter a number to roll a different die.\n"
              "Available dice: 4, 6, 8, 10, 12, 20, 100.\n"
              "Press 'q' to quit."
              "Turn off CAPS LOCK.")
    else:
        print("That is not a valid entry.\nPress 'h' for help.")
