#1st we need to define the questions, options, and correct answers
questions = [
    {
        "prompt": "What is Economics mainly concerned with?",
        "options": [
            "A. Studying unlimited resources.",
            "B. Studying how societies manage scarce resources.",
            "C. Studying political systems.",
            "D. Studying technological innovation."
        ],
        "answer": "B"
    },
    {
        "prompt": "What does scarcity mean in Economics?",
        "options": [
            "A. Resources are equally distributed.",
            "B. Human wants are limited.",
            "C. Resources are limited while wants are unlimited.",
            "D. Goods are expensive."
        ],
        "answer": "C"
    },
    {
        "prompt": "What is an opportunity cost?",
        "options": [
            "A. The monetary cost of a good.",
            "B. The cost of production.",
            "C. The value of the best alternative given up.",
            "D. The total cost of all alternatives."
        ],
        "answer": "C"
    },
    {
        "prompt": "Which of the following is a factor of production?",
        "options": [
            "A. Money.",
            "B. Labour.",
            "C. Consumption.",
            "D. Inflation."
        ],
        "answer": "B"
    },
    {
        "prompt": "What is the main objective of consumers?",
        "options": [
            "A. To maximize production.",
            "B. To minimize costs.",
            "C. To maximize satisfaction (utility).",
            "D. To control prices."
        ],
        "answer": "C"
    },
    {
        "prompt": "What happens to demand when the price of a good increases (ceteris paribus)?",
        "options": [
            "A. Demand increases.",
            "B. Demand decreases.",
            "C. Demand remains the same.",
            "D. Supply decreases."
        ],
        "answer": "B"
    },
    {
        "prompt": "What is Gross Domestic Product (GDP)?",
        "options": [
            "A. The total income of households.",
            "B. The total value of imports.",
            "C. The total value of goods and services produced in a country.",
            "D. The total value of exports."
        ],
        "answer": "C"
    },
    {
        "prompt": "What is inflation?",
        "options": [
            "A. A decrease in the general price level.",
            "B. An increase in wages.",
            "C. A sustained increase in the general price level.",
            "D. An increase in unemployment."
        ],
        "answer": "C"
    },
    {
        "prompt": "Which economic agent is responsible for providing public goods?",
        "options": [
            "A. Households.",
            "B. Firms.",
            "C. The State (Government).",
            "D. Banks."
        ],
        "answer": "C"
    },
    {
        "prompt": "What is unemployment?",
        "options": [
            "A. When people choose not to work.",
            "B. When people are unable to find a job despite actively looking for one.",
            "C. When wages are too low.",
            "D. When people retire."
        ],
        "answer": "B"
    }
]


#we will now define the run_test function
def run_test(questions):
    score = 0 #the student's initial score is zero
    for question in questions:# Loop through each question in the list of questions
        print(question["prompt"]) # Print the question text (the prompt)
        for option in question["options"]:# Loop through all the possible answer options for the question
            print(option)
        answer = input("Enter your answer (A, B, C, D): ").upper() # Ask the student for an answer and convert it to uppercase, this ensures that 'a' and 'A' are treated the same
        if answer == question["answer"]: # Check if the student's answer matches the correct answer
            print("Correct!\n") # Inform the student the answer is correct
            score += 1 # Increase the score by 1
        else:
            print("Wrong! The correct answer was", question["answer"], "\n") # Inform the user the answer is wrong and show the correct one

    #1st we need to define the questions, options, and correct answers
questions = [
    {
        "prompt": "What is Economics mainly concerned with?",
        "options": [
            "A. Studying unlimited resources.",
            "B. Studying how societies manage scarce resources.",
            "C. Studying political systems.",
            "D. Studying technological innovation."
        ],
        "answer": "B"
    },
    {
        "prompt": "What does scarcity mean in Economics?",
        "options": [
            "A. Resources are equally distributed.",
            "B. Human wants are limited.",
            "C. Resources are limited while wants are unlimited.",
            "D. Goods are expensive."
        ],
        "answer": "C"
    },
    {
        "prompt": "What is an opportunity cost?",
        "options": [
            "A. The monetary cost of a good.",
            "B. The cost of production.",
            "C. The value of the best alternative given up.",
            "D. The total cost of all alternatives."
        ],
        "answer": "C"
    },
    {
        "prompt": "Which of the following is a factor of production?",
        "options": [
            "A. Money.",
            "B. Labour.",
            "C. Consumption.",
            "D. Inflation."
        ],
        "answer": "B"
    },
    {
        "prompt": "What is the main objective of consumers?",
        "options": [
            "A. To maximize production.",
            "B. To minimize costs.",
            "C. To maximize satisfaction (utility).",
            "D. To control prices."
        ],
        "answer": "C"
    },
    {
        "prompt": "What happens to demand when the price of a good increases (ceteris paribus)?",
        "options": [
            "A. Demand increases.",
            "B. Demand decreases.",
            "C. Demand remains the same.",
            "D. Supply decreases."
        ],
        "answer": "B"
    },
    {
        "prompt": "What is Gross Domestic Product (GDP)?",
        "options": [
            "A. The total income of households.",
            "B. The total value of imports.",
            "C. The total value of goods and services produced in a country.",
            "D. The total value of exports."
        ],
        "answer": "C"
    },
    {
        "prompt": "What is inflation?",
        "options": [
            "A. A decrease in the general price level.",
            "B. An increase in wages.",
            "C. A sustained increase in the general price level.",
            "D. An increase in unemployment."
        ],
        "answer": "C"
    },
    {
        "prompt": "Which economic agent is responsible for providing public goods?",
        "options": [
            "A. Households.",
            "B. Firms.",
            "C. The State (Government).",
            "D. Banks."
        ],
        "answer": "C"
    },
    {
        "prompt": "What is unemployment?",
        "options": [
            "A. When people choose not to work.",
            "B. When people are unable to find a job despite actively looking for one.",
            "C. When wages are too low.",
            "D. When people retire."
        ],
        "answer": "B"
    }
]


#we will now define the run_test function
def run_test(questions):
    score = 0 #the student's initial score is zero
    for question in questions:# Loop through each question in the list of questions
        print(question["prompt"]) # Print the question text (the prompt)
        for option in question["options"]:# Loop through all the possible answer options for the question
            print(option)
        answer = input("Enter your answer (A, B, C, D): ").upper() # Ask the student for an answer and convert it to uppercase, this ensures that 'a' and 'A' are treated the same
        if answer == question["answer"]: # Check if the student's answer matches the correct answer
            print("Correct!\n") # Inform the student the answer is correct
            score += 1 # Increase the score by 1
        else:
            print("Wrong! The correct answer was", question["answer"], "\n") # Inform the user the answer is wrong and show the correct one

    if score >= 0.5*len(questions):  # After all questions are answered, check if the user passed
        print(f"You passed! You got {score} out of {len(questions)} questions correct. Congratulations!") # Inform the user that they passed the test and show their final score
    else:
        print(f" You failed! You got {score} out of {len(questions)} questions correct. Study harder!") # Inform the user that they failed the test and show their final score

run_test(questions) # Call the function and pass the list of questions to start the quiz:  # After all questions are answered, check if the user passed
        print(f"You passed! You got {score} out of {len(questions)} questions correct. Congratulations!") # Inform the user that they passed the test and show their final score
    else:
        print(f" You failed! You got {score} out of {len(questions)} questions correct. Study harder!") # Inform the user that they failed the test and show their final score


run_test(questions) # Call the function and pass the list of questions to start the quiz
