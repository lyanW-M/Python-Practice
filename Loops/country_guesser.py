# =====================================================================
# Task: Country Guessing Game
# =====================================================================

# VALUES
# TODO: Create a variable to store the correct country (e.g., "Italy").
# TODO: Create a variable to keep track of the user's current guess. 
#       (Hint: Start it as an empty string "" so the loop runs at least once!)


# LOOP
# TODO: Start a 'while' loop. 
#       The loop should keep running AS LONG AS the user's guess 
#       is NOT EQUAL to the correct country.
    
    # TODO: Ask the user for their guess and save it to your guess variable.
    #       (Remember: This changes the loop condition so it doesn't run forever!)
    
    # TODO: (Optional) Add an 'if' statement inside the loop.
    #       If they guessed wrong, print an encouraging message or an extra hint.
    #       If they guessed right, the loop will automatically exit on the next check!


# GAME OVER / WINNING MESSAGE
# TODO: Print a congratulatory message celebrating their win!

# ================================================================
# EXTENSION
# TODO: Add an introduction
# TODO: Add a scoring system (starts at 20, lose 1 point for each wrong guess)
# TODO: Add a lose condition (if score reaches 0)

#==================================================================
# EXPERT
# TODO: Make the game unique (use a list of countries and randomly select one)
# TODO: Add a play again option

import random

list = ["italy", "france", "spain", "germany", "japan", "brazil", "canada", "australia", "india", "china"]
answer = random.choice(list)
score = 10
guess = ""

print ("Welcome to the Country Guessing Game!")
print ("Try to guess the country I'm thinking of. You can do it!")
while answer != guess:
    guess = input("Enter your guess: ".lower().strip())
    if guess != answer:
        print("Wrong! Try again.")
        score -= 1
        if score == 0:
            print(f"Game over! You've run out of points. The correct answer was {answer}.")
            break
    elif guess == answer:
        print(f"Congratulations! You've guessed the country correctly with a score of {score}!")
        break


