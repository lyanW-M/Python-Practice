# Create a roller coaster access screener (determine if the user is allowed to ride)
# Rules:    They must be over 150cm and over 10 years old
#           They must not have a heart condition
#           OR they can ride if they have a VIP pass

# Get input





# Check conditions and output verdict




# ------------------------------
# EXTENSION
# Change your screener to work for 3 different rides (ask user which ride at the beginning) with different rules

# ------------------------------
# EXPERT
# Follow the same task (with extension), but use dictionaries to make the code more efficient
print("Coaster Ride 1 Rules: You must be over 150cm and over 10 years old. You must not have a heart condition. OR you can ride if you have a VIP pass.")
print("Coaster Ride 2 Rules: You must be over 120cm and over 8 years old. You must not have a heart condition. OR you can ride if you have a VIP pass.")
print("Coaster Ride 3 Rules: You must be over 100cm and over 6 years old. You must not have a heart condition. OR you can ride if you have a VIP pass.")

height = int(input("What is your height in cm? "))
age = int(input("What is your age? "))
heart_condition = input("Do you have a heart condition? (yes or no) ")
vip_pass = input("Do you have a VIP pass? (yes or no) ")

ride = input("Which ride would you like to go on? (1, 2 or 3): ")
if ride == "1":
    if (height > 150 and age > 10 and heart_condition == "no") or vip_pass == "yes":
        print("You can ride Coaster Ride 1!")
    else:
        print("Sorry, you do not meet the requirements for Coaster Ride 1.")
elif ride == "2":
    if (height > 120 and age > 8 and heart_condition == "no") or vip_pass == "yes":
        print("You can ride Coaster Ride 2!")
    else:
        print("Sorry, you do not meet the requirements for Coaster Ride 2.")
elif ride == "3":
    if (height > 100 and age > 6 and heart_condition == "no") or vip_pass == "yes":
        print("You can ride Coaster Ride 3!")
    else:
        print("Sorry, you do not meet the requirements for Coaster Ride 3.")