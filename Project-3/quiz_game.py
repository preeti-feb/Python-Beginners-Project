print("-" * 40)
print("GENERAL KNOWLEDGE QUIZ")
print("-" * 40)


print("\nWelcome to quiz game")
print("\nTotal Questions = 5")
print("Choose the correct option (A, B, C)")



questions = [
    {
        "question": "What is the capital of the USA?",
        "A": "New York",
        "B": "Washington, D.C.",
        "C": "Los Angeles",
        "D": "Chicago",
        "answer": "B"
    },
    {
        "question": "Which country is known as the Land of the Rising Sun?",
        "A": "China",
        "B": "India",
        "C": "Japan",
        "D": "South Korea",
        "answer": "C"
    },
    {
        "question": "Who was the first person to walk on the Moon?",
        "A": "Neil Armstrong",
        "B": "Albert Einstein",
        "C": "Yuri Gagarin",
        "D": "Galileo Galilei",
        "answer": "A"
    },
    {
        "question": "What does CPU stand for?",
        "A": "Computer Personal Unit",
        "B": "Central Processing Unit",
        "C": "Central Program Utility",
        "D": "Computer Processing User",
        "answer": "B"
    },
    {
        "question": "Who wrote Romeo and Juliet?",
        "A": "Charles Dickens",
        "B": "William Wordsworth",
        "C": "Jane Austen",
        "D": "William Shakespeare",
        "answer": "D"
    }
]


score = 0

for q in questions:
    print("\n" + q["question"])
    print("A.", q["A"])
    print("B.", q["B"])
    print("C.", q["C"])
    print("D.", q["D"])
    user_answer = input("\nEnter your answer A, B, C or D: ").upper()

    if user_answer == q["answer"]:
        score += 1
        print("Correct Answer!")

    else:
        print("Incorrect Answer!")
        print("Correct answer:", q["answer"])


if score >= 3:
    print(f"\nYour score is: {score}. And your basic knowelege is good.")

else:
    print(f"\nYour score is {score}. Improve your basic knowledge.")


print("Keep learning, Happy Learning ❤️ !")
