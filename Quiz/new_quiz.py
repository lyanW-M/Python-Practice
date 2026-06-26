# Introduction
print("WELCOME TO THE QUIZ SHOW!")
print("Answer these 7 questions in order to win.... NOTHING!")

while True:

    # Score
    score = int(0)

    # Question 1
    q1 = input("What is the capital of India? A) New Delhi B) Mumbai C) Kolkata D) Chennai\n")
    q1 = q1.upper().strip()
    if q1 == "A" or q1 == "NEW DELHI":
        print("CORRECT")
        score += 1
    else:
        print("WRONG!!!")

    # Question 2
    q2 = input("What is 1*1? A) 0 B) 1 C) 2 D) 3\n")
    q2 = q2.upper().strip()
    if q2 == "B" or q2 == "ONE" or q2 == "1":
        print("CORRECT")
        score += 1
    else:
        print("WRONG!!!")

    # Question 3
    q3 = input("Winner says what A) What B) Who C) Where D) When\n")
    q3 = q3.upper().strip()
    if q3 == "A" or q3 == "WHAT":
        print("CORRECT")
        score += 1
    else:
        print("WRONG!!!")

    # Question 4
    q4 = input("Is Nivedh aura? A) Yes B) No C) Maybe D) I don't know\n")
    q4 = q4.upper().strip()
    if q4 == "B" or q4 == "NO":
        print("CORRECT")
        score += 1
    else:
        print("WRONG!!!")

    # Question 5
    q5 = input("What is the capital of France? A) Paris B) London C) Berlin D) Madrid\n")
    q5 = q5.upper().strip()
    if q5 == "A" or q5 == "PARIS":
        print("CORRECT")
        score += 1
    else:
        print("WRONG!!!")  

    # Question 6
    q6 = input("What is the largest planet in our solar system? A) Earth B) Mars C) Jupiter D) Saturn\n")
    q6 = q6.upper().strip()
    if q6 == "C" or q6 == "JUPITER":
        print("CORRECT")
        score += 1
    else:
        print("WRONG!!!")

    # Question 7
    q7 = input("What is the chemical symbol for water? A) H2O B) CO2 C) O2 D) N2\n")
    q7 = q7.upper().strip()
    if q7 == "A" or q7 == "H2O":
        print("CORRECT")
        score += 1
    else:
        print("WRONG!!!")

    # Final Score
    print(f"Your final score is {score}\n")
    if score == 7:
        print("Perfect score, 7/7")
    elif score < 7 and score >= 5:
        print(f"Great job! You scored {score}/7, that's a good score!")
    elif score == 6:
        print(f"SIX SEVEN! SIX SEVENNNNNNNN, {score}/7!")
    elif score == 0:
        print(F"YOU SUCK!!!! {score}/7, HOW DID YOU MAKE IT THIS FAR IN LIFE!?")
    else:
        print(f"Your score is {score} out of 7, better luck next time!")

    # Replay Option
    while True:
        replay = input("Do you want to play again? (yes/no)\n")
        replay = replay.upper().strip()
        if replay == "YES":
            print("Starting a new game...")
            break
        elif replay == "NO":
            print("Thanks for playing! Goodbye!")
            exit()
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
            continue