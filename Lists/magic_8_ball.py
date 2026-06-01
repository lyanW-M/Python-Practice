# =====================================================================
# PROJECT: The Magic 8-Ball Fortune Teller
# Create a program that gives random responses to yes/no questions
# =====================================================================

# TOOLS
# TODO: Import the 'random' module so we can pick a random index later.
import random


# RESPONSES
# TODO: Create a list called 'responses' that contains at least 8 different 
#       8-ball answers (strings). There should be positive answers, negative answers and neutral answers.
#       Examples: "Yes, definitely!", "Ask again later.", "Outlook not so good."
commonballResponses = ["Yes, definitely!", "No", "Maybe", "Ask again later.", "Definitely!", "Outlook not so good.", "Very doubtful.", "Signs point to yes."]
rareballResponses = ["You will find true love soon!", "Your future is bright!", "A surprise is waiting for you around the corner!", "You will achieve your dreams!"]

# MAIN LOOP
# TODO Create an infinite loop
while True:
    
    # TODO: Ask the user to type in a Yes/No question about their future and save it in a variable.
    #       (Or tell them to type 'quit' to leave).
    question = input("Ask the Magic 8-Ball a Yes/No question (or type 'quit' to leave): ").lower().strip()
    
    # Check if the user wants to exit and break from the loop if they do.
    if question.lower().strip() == 'quit':
        print("Goodbye!")
        break
        
    # RANDOM REPSONSE
    # TODO: Step A: Calculate the last valid index of your list.
    #       (Remember: If a list has 5 items, the indexes are 0, 1, 2, 3, 4).
    #       Use random.randint() to get a number between 0 and that last index.

    ball_selection = random.choices(["common", "rare"], weights=[0.8, 0.2], k=1)[0]
    
    # Step B: Pick a random answer from the chosen pool and print it
    if ball_selection == "common":
        random_index = random.randint(0, len(commonballResponses) - 1)
        response = commonballResponses[random_index]
    else:
        random_index = random.randint(0, len(rareballResponses) - 1)
        response = rareballResponses[random_index]
        
    print(response)
    # TODO Print the result

# TODO Say goodbye to let them know the program has ended.

# ==================================================
# EXTENSION
# Common and rare responses
# TODO Split your responses into 2 lists. A common responses list and a rare responses list
# TODO Use random.random() or randint() to get a percentage
# TODO Check if the number is lower than 0.8 and use the common list to give a response if it is
# TODO Otherwise use the rare list



# ===================================================
# EXPERT
# Try creating a magic eight ball that gives random responses based on the question (eg. positive, negative, snarky, funny responses)
# TODO Create a dictionary (or multiple lists)
# TODO Check for key words in the question to decide what type of response. Eg. "will I" has positive responses, short quest