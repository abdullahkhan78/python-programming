# ---------------- Quiz Game ----------------

# List of questions with options and answers
questions = [
    {
        "question": "What is the capital of Pakistan?",
        "options": ["A. Lahore", "B. Islamabad", "C. Karachi", "D. Peshawar"],
        "answer": "B"
    },
    {
        "question": "Which language is used for web development?",
        "options": ["A. Python", "B. HTML", "C. C++", "D. Java"],
        "answer": "B"
    },
    {
        "question": "Which one is a programming language?",
        "options": ["A. Snake", "B. Tiger", "C. Java", "D. Apple"],
        "answer": "C"
    },
    {
        "question": "2 + 2 = ?",
        "options": ["A. 3", "B. 4", "C. 5", "D. 6"],
        "answer": "B"
    },
    {
        "question": "Which company created Python?",
        "options": ["A. Google", "B. Microsoft", "C. Facebook", "D. Guido van Rossum"],
        "answer": "D"
    }
]

score = 0  # keep track of correct answers

print("========= Welcome to the Quiz Game =========\n")

# Loop through all questions
for q in questions:
    print(q['question'])
    for option in q["options"]:
        print(option)
    answer = input('Enter your answer (A, ,B ,C ,D): ').upper()
    if answer == q["answer"]:
        print("Correct")
        score += 1
    else:
        print(f"Wrong! The correct answer is {q("answer")}")    


# Show final result
print("========= Quiz Finished =========")
print(f"Yoour final score: {score} out of {len(questions)}")


if score == len(questions):
    print("Excellent you got all correct! ")
elif score >= 3:
    print("Goob job!")
else:
    print("Keep practiciing!")        

