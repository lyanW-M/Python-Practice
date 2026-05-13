# Write a 'what animal are you' quiz. 
# You can base this on the picture from last lesson, but make it simpler - 
# 3 questions and 4 animals.

print("WHAT ANIMAL ARE YOU QUIZ!!!")

# Ask your user a question about themselves, giving them 2 options

q1 = input("Are you a sigma or an alpha?")

# Check if they picked the first option

if q1 in["Alpha", "alpha", "ALPHA"]:

    # Ask the next question

    q11 = input("Are you team triple T or skibidi toilet?")

    # Check if they picked the first option

    if q11 in["Triple T", "triple t", "Triple t", "TRIPLE T"]:

        # Tell them they're animal 1

        print("You are Awakened Bahamut Cat")

    # Otherwise

    elif q11 in["Skibidi toiloet", "SKIBIDI TOILET", "skibidi toilet"]:

        # Tell them they're animal 2

        print("You are Hermit Cat")


# Otherwise

elif q1 in["sigma", "SIGMA", "Sigma"]:

    # Ask the next question

    q12 = input("Are you team triple T or team skibidi toilet?")

    # Check if they picked the first option

    if q12 in["Triple T", "triple t", "Triple t", "TRIPLE T"]:

        # Tell them they're animal 3

        print("You're Commmander Cat")

    # Otherwise

    elif q12 in["Skibidi toiloet", "SKIBIDI TOILET", "skibidi toilet"]:

        # Tell them they're animal 4

        print("You're Relentless Gladios") 

# __________________________

# EXTENSION
# Extend the quiz so there are 8 possible animals

# __________________________

# EXTENSION 2
# Create a 'Which ??? are you?' Quiz
# This time allow all questions to have 4 possible answers (a,b,c and d) 
# and tally how many times they choose each
# Determine what they are at the end using the letter with the highest tally.
# Eg. If they picked mostly As, maybe they are Pikachu.