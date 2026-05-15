#Introduction
print("WELCOME TO THE QUIZ SHOW!")
print("Answer these 5 questions in order to win.... NOTHING!")

#Score
score = int(0)

#Question 1
q1 = input("First question; How do you spell cat?\n")
if q1 in ["cat", "CAT", "Cat"]:
    print("CORRECT")
    score += 1
else:
    print("WRONG!!!")

#Question 2
q2 = input("What is the capital of India?\n")
if q2 in ["New Delhi", "NEW DELHI", "new delhi"]:
    print("CORRECT")
    score += 1
else:
    print("WRONG!!!")

#Question 3
q3 = input("What is 1*1?\n")
if q3 in ["1", "one", "One", "ONE"]:
    print("CORRECT")
    score += 1
else:
    print("WRONG!!!")

#Question 4
q4 = input("Winner says what?\n")
if q4 in ["What", "what", "WHAT"]:
    print("CORRECT")
    score += 1  
else:
    print("WRONG!!!")

#Question 5
q5 = input("Is Nivedh aura?\n")
if q5 in ["No", "no", "NO", "nah", "Nah", "NAH"]:
    print("CORRECT")
    score += 1
else:
    print("WRONG!!!")

#Final Score
print("Your final score is ", score, "/5")

if score == 5:
    print("Perfect score, 5/5")
else:
    print("You're score is ", score, "out of 5, better luck next time!")
