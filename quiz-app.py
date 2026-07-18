import random

CATEGORY_FILES = {
    "1": ("Python Language", "python_questions"),
    "2": ("Indian History", "history_questions"),
    "3": ("Indian Geography", "geography_questions"),
    "4": ("Current Affairs", "current_affairs_questions")
}

# ---------------- LOAD QUESTIONS ----------------
def load_questions(module_name):
    module = __import__(module_name)
    return module.questions

# ---------------- CONDUCT QUIZ ----------------
def conduct_quiz(student_name, questions, num_questions):
    score = 0
    random.shuffle(questions)
    selected_questions = questions[:num_questions]

    print(f"\n===== QUIZ FOR {student_name.upper()} =====")

    for idx, q in enumerate(selected_questions, start=1):
        print(f"\nQ{idx}. {q['question']}")
        for i, option in enumerate(q["options"], start=1):
            print(f"{i}. {option}")

        choice = input("Enter your answer (1-4): ").strip()

        if choice == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! Correct answer: {q['answer']}")

    print(f"\n{student_name}'s Score: {score}/{num_questions}")
    return score

# ---------------- MAIN PROGRAM ----------------
print("===== QUIZ APPLICATION =====\n")

print("Select Category:")
for key, value in CATEGORY_FILES.items():
    print(f"{key}. {value[0]}")

category_choice = input("Enter category choice (1-4): ")

if category_choice not in CATEGORY_FILES:
    print("Invalid category!")
    exit()

category_name, module_name = CATEGORY_FILES[category_choice]
questions = load_questions(module_name)

num_students = int(input("\nEnter number of participants: "))
num_questions = int(input("Enter number of questions per student: "))

if num_questions > len(questions):
    print("Not enough questions in database!")
    exit()

results = {}

print(f"\n===== STARTING QUIZ: {category_name} =====")

for i in range(1, num_students + 1):
    student_name = input(f"\nEnter name of student {i}: ")
    score = conduct_quiz(student_name, questions.copy(), num_questions)
    results[student_name] = score

# ---------------- FINAL SUMMARY ----------------
print("\n===== FINAL RESULTS =====")

sorted_results = sorted(results.items(), key=lambda x: x[1], reverse=True)

print(f"{'Rank':<6}{'Student':<20}{'Score'}")
print("-" * 35)

for idx, (student, score) in enumerate(sorted_results, start=1):
    print(f"{idx:<6}{student:<20}{score}")

print("\nQuiz Completed. Thank you!")
