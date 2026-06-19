"""
PROGRAM: Geometry Helper
This program helps to calculate the area and circumference of a rectangle
"""

####### INSTRUCTIONS ########
# Complete the code by writing functions for calculating the area and circumference 
# taking the user input and returning it, 
# and calling each function based on user choice


# =====================================================================
# FUNCTIONS
# =====================================================================

# TODO ------->>>> Write a function here for calculating the area of a rectangle using passed values. 
# TODO ------->>>> Return the result.


# TODO ------->>>> Write a function here for calculating the circumference using passed values. 
# TODO ------->>>> Return the result.

def calculate_area():
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    area = length * width
    print(f"The area of the rectangle is: {area}")

def calculate_circumference():
    choice_circumference = input("Do you want to calculate the circumference with the radius or diameter? (Enter 'radius' or 'diameter'): ").lower().strip()
    if choice_circumference == "radius":
        radius = float(input("Enter the radius of the circle: "))
        circumference = 2 * 3.14159 * radius
        print(f"The circumference of the circle is: {circumference}")
    elif choice_circumference == "diameter":
        diameter = float(input("Enter the diameter of the circle: "))
        circumference = 3.14159 * diameter
        print(f"The circumference of the circle is: {circumference}")
    else:
        print("Invalid choice. Please enter 'radius' or 'diameter'.")

while True:
    print("Welcome to the Geometry Helper!")
    print("Choose a calculation to perform:")
    print("1. Area of a Rectangle")
    print("2. Circumference of a Circle")
    print("3. Exit")
    choice = input("Enter your choice (1 or 2 or 3): ")
    if choice == "1":
        calculate_area()
    elif choice == "2":
        calculate_circumference()
    elif choice == "3":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
# =====================================================================
# EXECUTION
# =====================================================================

