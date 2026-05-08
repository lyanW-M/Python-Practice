#Introduction
print("WELCOME TO THE QUIZ SHOW!")
print("Answer these 5 questions in order to win.... NOTHING!")

#Question 1
q1 = input("First question; How do you spell cat?\n")
if q1 in ["cat", "CAT", "Cat"]:
    print("CORRECT")
else:
    print("WRONG!!!")

#Question 2
q2 = input("What is the capital of India?\n")
if q2 in ["New Delhi", "NEW DELHI", "new delhi"]:
    print("CORRECT")
else:
    print("WRONG!!!")

#Question 3
q3 = input("What is 1*1?\n")
if q3 in ["1", "one", "One", "ONE"]:
    print("CORRECT")
else:
    print("WRONG!!!")

#Question 4
q4 = input("Winner says what?\n")
if q4 in ["What", "what", "WHAT"]:
    print("CORRECT")
else:
    print("WRONG!!!")

#Question 5
q5 = input("Is Nivedh aura?\n")
if q5 in ["No", "no", "NO", "nah", "Nah", "NAH"]:
    print("CORRECT")
else:
    print("WRONG!!!")