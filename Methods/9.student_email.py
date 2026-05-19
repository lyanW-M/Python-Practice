# Create a student email creator that uses first and lat name plus id
# eg. smithjohn123@fake.school.nz

# Get input (first, last, id) and save in variables




# Strip input to remove accidental spaces and turn names into lowercase (resave in variables)




# Output the final email address


# --------------------------------

# EXTENSION
# Create a temporary password to output as well
# It should be their names in all uppercase and their id divided by 10

# --------------------------------

# EXPERT
# Create a WSCW email creator
# Get the users first and last name, then randomly generate an ID number (8 digits long)
# Output the email addess (lastf.wsc.school.nz) 
# - you'll need to strip down the first name to just first letter
# Output their id number
# Output a temporary password (all uppercase). You can choose how you create this, 
# but it needs to be unique for each user
import random

first =input("What is your first name?".strip().lower())
last = input("What is your last name?".strip().lower())
id = random.randint(1000,9999)
email = last + first + str(id) + "@lastf.wsc.school.nz"
print("Your email address is: ", email)
