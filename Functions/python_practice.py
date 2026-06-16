"""
PROGRAM: Menu
This starts with a menu so users can run 1 of 3 different programs:
1.
2.
3.
"""

# INSTRUCTIONS
# TODO Create a menu that will run three different programs based on user input.
# TODO Each program will need to be its own function OR check out the EXPERT instructions below.

import random

def random_number_generator():
    print("Random Number Generator")
    print("Generating a random number between 1 and 100...")
    print(random.randint(1, 100))

def coin_flip():
    print("Coin Flip")
    print("Flipping a coin...")
    flip = random.choice(["Heads", "Tails"])
    print(f"The coin landed on {flip}!")

def dice_roll():
    print("Dice Roll")
    print("Rolling a six-sided die...")
    print(f"You rolled a {random.randint(1, 6)}!")

print("Welcome to the Menu Program!")
print("Choose a program to run:")
print("1. Random Number Generator")
print("2. Coin Flip")
print("3. Dice Roll")

choice = input("Enter your choice (1, 2, or 3): ")

while choice not in ["1", "2", "3"]:
    if choice == "1":
        random_number_generator()
    elif choice == "2":
        coin_flip()
    elif choice == "3":
        dice_roll()
    else:
        print("Invalid choice. Please try again.")

#===============================
#===============================
# EXTENSION
# TODO Go back to each program you chose and structure them with functions. 
# TODO Then recopy them over as multiple functions (rather than one)
# NOTE The main() function in your programs can be renamed as run_program_name() so it doesn't clash with this program's main()
#===============================
#===============================
# EXPERT
# TODO Instead of bringing the code from other programs into this file, use import to import locally.
# You'll need to start by editing your other files so all their code is in function with a main() function
# NOTE Check this out for info on importing locally: https://github.com/Year-11-Programming/Python-Practice-Projects/wiki/Import-Locals