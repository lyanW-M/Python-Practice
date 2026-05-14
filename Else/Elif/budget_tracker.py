### Budget Tracker ###
# Create a budget tracker that gives financial recommendation around an item

# Create a constant to hold your budget
budget = input("What is your budget?")
# Create a constant to hold your savings (percentage) goal
savings = input("What is your savings goal percentage?")    

# Ask user for item name and save in variable
item = input("What item are you thinking of buying?")
# Ask user for cost and save in variable
cost = input("How much does it cost?")
# Change the cost into an integer
cost = int(cost)

# Calculate the percentage of budget (cost / budget) * 100
percentage = (cost / int(budget)) * 100
# Tell your user the percentage of your budget
print("This item is ", percentage, "% of your budget")

# Check if percentage is 0 and say it's free if it is
if percentage == 0:
    print("This item is free, go get it!")

# Check if the percentage is less then 10 and say it's a small treat so enjoy
elif percentage < 10:
    print("This is a small treat, go get it and enjoy!")

# Check if it is less than 50 percent and if it is tell them it's a major spend and should sleep on it
elif percentage < 50:
    print("This is a major spend, you should sleep on it and see if you still want it in the morning")

# Check if it's over 100 and if it is tell them they don't have enough money
elif percentage > 100:
    print("You don't have enough money for this item, you should save up for it")

# Otherwise, tell them it costs way too much and isn't worth it
else:
    print("This item costs way too much and isn't worth it, you should save up for it or find a cheaper alternative")

# _______________________

# EXTENSION
# Include an item type question and change answers based on this. 
# Eg. food shouldn't cost as much as a bill so if it's a food, 
# tell them to not buy it at a lower percentage


# _______________________

# EXPERT
# Try to create a budget tracker that saves data in a file 
# so the remaining_budget can be updated every time the program is used
# You will need to create a save.txt file to go with this (keep it in the same folder)
# If you're not sure how to do this check here: https://www.w3schools.com/python/python_file_write.asp 

