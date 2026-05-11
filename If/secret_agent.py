### Secret Agent Login
# Create a login process for a secret agent

# Ask for the user's name and save it in a variable

# Ask for the password and save it in a variable

# Check if the password == 'Falcon'

    # Ouput that access has been granted and welcome user using their name

    # Ask for the user's age and save it in a variable

    # Change the age into an integer

    # If the user's age is under 13, tell them they are a spy in training

    # If their age is under 18, tell them they are a junior spy

    # If their age is 18 or over, tell them they are a Field Agent

# Output a goodbye

name = input("What is your name?")
password = input("What is the password?")

if password == ("Falcon"):
    print("Welcome, ", name)
else:
    print("ALERT ALERT! A SPY IS IN OUR BASE!!!")

age = int(input("What is your age?"))

if age < 13:
    print("You're a Spy in Training")
elif age < 18:
    print("You're a Junior Spy")
elif age >= 18:
    print("You're a Field Agent")

print("See you on the field!")





# ___________________________

# EXTENSION

# Ask more questions to give your spy more information
# Look up how to use 'and' and 'or' to force more conditions (eg. they must be one of 3 users AND get the password correct)

CEOname = input("Wait hold up, by any chance do you know one of our 3 CEO's names?")

if CEOname == ["Grey", "Gray", "Gru"]:
    print("Oh cool cool")
else:
    print("Boring")


# ___________________________

# EXPERT (For those who already know python)

# Create a SPY ID GENERATOR
# Your user must login using the correct password to access the generator
# Use a bunch of questions to generate an id. Eg. If their name has 4 or fewer