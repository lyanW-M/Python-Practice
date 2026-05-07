print("Hello" + " World")
print("Hello World\n" * 5)

# Print the answers to the following questions. Get the computer to do the math for you!

# What is 376 + 209 + 44439?
print(376 + 209 + 44439)

# What is 2345678 - 678 - 1?
print(2345678 - 678 - 1)

# What is 345 divided by 34?
print(345 / 34)

# What is 567 * 34 * 3?
print(567 * 34 * 3)

# Print 'hello' 32 times.
print("hello" * 32)

# -------------------------

# EXTENSION

# What is 2345 / 766 rounded to the nearest whole number?
print(2345 // 766)

# What is 456 to the power of 23?
print(456 ** 23)

# What is the remainder if you divide 345 by 32?
print(345 % 32)

# --------------------------

# EXPERT (for those who already know some Python)
# Create a simple calculator
# GOAL: The user chooses Add, Subtract, Multiply or Divide, then inputs 2 numbers
#       The computer will output the result.
# (Optional) Make sure the user can only input numbers

operations = input("What operation would you like to choose? Addition, Subtraction, Multiplication, Division\n")

if operations in ["addition", "Addition"]:
    add1 = int(input("Type in the first number\n"))
    add2 = int(input("Type in the second number\n"))
    print(add1 + add2, "is your answer")

elif operations in ["subtraction", "Subtraction"]:
    sub1 = int(input("Type in the first number\n"))
    sub2 = int(input("Type in the second number\n"))
    print(sub1 - sub2, "is your answer")

elif operations in ["multiplication", "Multiplication"]:
    mult1 = int(input("Type in the first number\n"))
    mult2 = int(input("Type in the second number\n"))
    print(mult1 * mult2, "is your answer")

elif operations in ["division", "Division"]:
    div1 = int(input("Type in the first number\n"))
    div2 = int(input("Type in the second number\n"))
    print(div1 / div2, "is your answer")

else:
    print("Filthy monkey, can't even type properly")


