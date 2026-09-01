import random


# Question Bank

QUESTIONS = [
    {
        "question": "What is the output of 5 + 3?",
        "options": {
            "A": "6",
            "B": "7",
            "C": "8",
            "D": "9"
        },
        "answer": "C"
    },

    {
        "question": "Which data type is used to store text in Python?",
        "options": {
            "A": "int",
            "B": "str",
            "C": "float",
            "D": "bool"
        },
        "answer": "B"
    },

    {
        "question": "Which keyword is used to define a function?",
        "options": {
            "A": "function",
            "B": "define",
            "C": "def",
            "D": "func"
        },
        "answer": "C"
    },

    {
        "question": "Which symbol is used for a single-line comment in Python?",
        "options": {
            "A": "//",
            "B": "/*",
            "C": "#",
            "D": "--"
        },
        "answer": "C"
    },

    {
        "question": "Which loop is commonly used to iterate through a list?",
        "options": {
            "A": "for",
            "B": "repeat",
            "C": "loop",
            "D": "foreach"
        },
        "answer": "A"
    },

    {
        "question": "Which keyword is used to handle exceptions?",
        "options": {
            "A": "catch",
            "B": "error",
            "C": "except",
            "D": "handle"
        },
        "answer": "C"
    },

    {
        "question": "Which operator is used for exponentiation in Python?",
        "options": {
            "A": "^",
            "B": "**",
            "C": "//",
            "D": "%%"
        },
        "answer": "B"
    },

    {
        "question": "Which function is used to get the length of a list?",
        "options": {
            "A": "length()",
            "B": "size()",
            "C": "count()",
            "D": "len()"
        },
        "answer": "D"
    },

    {
        "question": "Which data structure stores key-value pairs?",
        "options": {
            "A": "List",
            "B": "Tuple",
            "C": "Dictionary",
            "D": "Set"
        },
        "answer": "C"
    },

    {
        "question": "Which method adds an item to the end of a list?",
        "options": {
            "A": "add()",
            "B": "append()",
            "C": "insert()",
            "D": "push()"
        },
        "answer": "B"
    },

    {
        "question": "Which keyword is used for a condition?",
        "options": {
            "A": "if",
            "B": "when",
            "C": "check",
            "D": "condition"
        },
        "answer": "A"
    },

    {
        "question": "Which file mode is used to read a file?",
        "options": {
            "A": "w",
            "B": "a",
            "C": "r",
            "D": "x"
        },
        "answer": "C"
    },

    {
        "question": "Which keyword is used when a loop should skip to its next iteration?",
        "options": {
            "A": "skip",
            "B": "continue",
            "C": "next",
            "D": "pass"
        },
        "answer": "B"
    },

    {
        "question": "What does float() do?",
        "options": {
            "A": "Converts a value to a floating-point number",
            "B": "Rounds a number",
            "C": "Converts a value to an integer",
            "D": "Creates a list"
        },
        "answer": "A"
    },

    {
        "question": "Which statement is used to stop a loop?",
        "options": {
            "A": "stop",
            "B": "exit",
            "C": "break",
            "D": "end"
        },
        "answer": "C"
    }
]


# Constants

QUESTIONS_PER_ROUND = 10
HIGH_SCORE_FILE = "highscore.txt"


# Helper Functions

def line():
    print("-" * 65)


def title(text):
    line()
    print(text.center(65))
    line()


def pause():
    input("\nPress Enter to continue...")


# High Score Functions

def load_high_score():
    """
    Load the highest score from the high score file.
    Return 0 if the file does not exist or contains invalid data.
    """

    try:

        with open(HIGH_SCORE_FILE, "r") as file:

            score = int(file.read().strip())

            return score

    except (FileNotFoundError, ValueError):

        return 0


def save_high_score(score):
    """Save the new high score to the file."""

    try:

        with open(HIGH_SCORE_FILE, "w") as file:

            file.write(str(score))

    except Exception as error:

        print("Unable to save high score.")
        print(error)


# Ask Question

def ask_question(question_number, question):
    """
    Display one question and return True if the answer is correct.
    """

    print()
    print(f"Question {question_number}")
    line()

    print(question["question"])
    print()

    for letter, option in question["options"].items():

        print(f"{letter}. {option}")

    line()

    while True:

        answer = input("Your answer (A/B/C/D): ").strip().upper()

        if answer in ["A", "B", "C", "D"]:
            break

        print("Invalid answer.")
        print("Please enter A, B, C, or D.")

    if answer == question["answer"]:

        print("\nCorrect!")
        return True

    correct_letter = question["answer"]
    correct_option = question["options"][correct_letter]

    print("\nIncorrect.")
    print(
        f"Correct answer: "
        f"{correct_letter}. {correct_option}"
    )

    return False


# Grade Function

def get_grade(score, total_questions):

    percentage = (score / total_questions) * 100

    if percentage >= 90:
        grade = "A"
        message = "Excellent! Outstanding performance!"

    elif percentage >= 80:
        grade = "B"
        message = "Great job! Keep it up!"

    elif percentage >= 70:
        grade = "C"
        message = "Good effort! Keep practicing."

    elif percentage >= 60:
        grade = "D"
        message = "You passed, but there is room for improvement."

    else:
        grade = "F"
        message = "Keep practicing. You can improve!"

    return percentage, grade, message


# ==========================================================
# Show Results
# ==========================================================

def show_results(score, total_questions):

    title("QUIZ RESULTS")

    percentage, grade, message = get_grade(
        score,
        total_questions
    )

    print(f"Correct Answers : {score}")
    print(f"Total Questions : {total_questions}")
    print(f"Percentage      : {percentage:.2f}%")
    print(f"Grade           : {grade}")

    line()

    print(message)

    line()


# Play One Quiz

def play_quiz(high_score):

    title("PYTHON QUIZ GAME")

    print(f"Questions in this round : {QUESTIONS_PER_ROUND}")
    print(f"Current High Score      : {high_score}")
    print()

    input("Press Enter to start the quiz...")

    # Make a copy so the original question bank is not permanently changed.
    questions = QUESTIONS.copy()

    # Randomize the question order.
    random.shuffle(questions)

    # Take only the required number of questions.
    selected_questions = questions[:QUESTIONS_PER_ROUND]

    score = 0

    for number, question in enumerate(selected_questions, start=1):

        correct = ask_question(
            number,
            question
        )

        if correct:
            score += 1

    print()

    show_results(
        score,
        len(selected_questions)
    )

    if score > high_score:

        print("\n*** NEW HIGH SCORE! ***")

        print(
            f"You achieved a new high score of "
            f"{score}/{len(selected_questions)}!"
        )

        save_high_score(score)

        high_score = score

    else:

        print(
            f"\nHigh Score: "
            f"{high_score}/{len(selected_questions)}"
        )

    return high_score


# Play Again

def play_again():

    while True:

        answer = input(
            "\nWould you like to play again? (yes/no): "
        ).strip().lower()

        if answer == "yes" or answer == "y":

            return True

        if answer == "no" or answer == "n":

            return False

        print("Please enter yes/y or no/n.")


# Main Function

def main():

    high_score = load_high_score()

    title("WELCOME TO THE PYTHON QUIZ GAME")

    print(
        f"There are {len(QUESTIONS)} questions "
        f"in the question bank."
    )

    print(
        f"Each round contains "
        f"{QUESTIONS_PER_ROUND} questions."
    )

    print(
        f"Current High Score: "
        f"{high_score}/{QUESTIONS_PER_ROUND}"
    )

    while True:

        high_score = play_quiz(high_score)

        if not play_again():

            print("\nThank you for playing!")
            print("Keep learning Python!")

            break


# Program Entry Point

if __name__ == "__main__":
    main()