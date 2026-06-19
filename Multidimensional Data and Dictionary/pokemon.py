# =====================================================================
# PROJECT: Pokemon
# Create a battle program where you battle a random pokemon
# =====================================================================

# TODO Import random module
import random
# Wild Pokemon
# TODO Create a multidimensional list that holds 4 pokemon names and their max health (you choose)
pokemons = [["Giratina", 500], ["Darkrai", 350], ["Glimmora", 370], ["Jinx", 270]] 
# User Pokemon
# TODO Create a multidimensional list that holds 4 pokemon attacks and their different damage
attacks = [["Shadow Ball", 80], ["Dark Pulse", 80], ["Ominous Wind", 50], ["Dragon Claw", 80]]

# TODO Create a variable to hold a randomised wild pokemon

wild_pokemon = random.choice(pokemons)
# TODO Tell the user what pokemon they're facing
encounter = input("A wild " + wild_pokemon + " has appeared! Do you want to battle it? (yes/no)").lower().strip()
if encounter == "yes":
    print("You chose to battle the " + wild_pokemon + "!")
# TODO Create a while loop that continues until current health <= 0
while wild_pokemon > 0:
    # TODO Ask the user which attack they'd like to use (list all 4 options, numbered); save input
    attack_choice = input("Which attack would you like to use? (1. Shadow Ball, 2. Dark Pulse, 3. Ominous Wind, 4. Dragon Claw)").strip().lower()
    # TODO Use try except to ensure the user has input a number; if they didn't tell them so and then use 'continue' to restart the loop
    # TODO Using the number, get the attack damage value and minus it from current health

# TODO Tell the user they defeated the pokemon

# ====================================================
# EXTENSION
# NOTE: Only do the extension once you have completed the project update (with dictionaries)

# TODO: Give your wild pokemon each an attack value as well, then allow it to attack the user back each turn (You'' need a player health)
# TODO: Change your 'user pokemon' to a list of different pokemon they can choose from. Each pokemon will have their own list of attacks.
# TODO: Give all pokemon a type. Create a new dictionary of types that each has a dict