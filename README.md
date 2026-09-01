# 🐍 Python Quiz Game

## CloudExify Python Internship — Month 2, Project 3

### Student Information

**Name:** Muhammad Anees  
**Reg. No:** CX-INT-2026-PY-0303

---

## 📌 Project Overview

The Python Quiz Game is a command-line application developed as part of the CloudExify Python Internship. It presents the player with multiple-choice questions based on fundamental Python programming concepts.

The program displays questions one at a time, accepts and validates the user's answers, provides immediate feedback, calculates the final score and percentage, assigns a letter grade, and keeps track of the highest score achieved.

The game can also be played repeatedly. Each new round selects questions in a randomized order, making every session different.

This project is part of **Month 2** of the internship and introduces Python's built-in `random` module while continuing to use concepts learned during Month 1, such as functions, loops, conditional statements, dictionaries, lists, and file handling.

---

## 🎯 Why This Project Was Useful

This project brought several Python concepts together into an interactive application.

Unlike projects that mainly store and display information, the quiz game required careful management of program flow. The application needs to display questions, accept user input, validate that input, determine whether the answer is correct, update the score, and finally present the results.

Another important aspect was persistent high-score storage. The program saves the best score in a text file, allowing the score to remain available even after the application is closed and started again.

---

## 🎲 Random Module

One of the main new concepts introduced in this project is Python's built-in `random` module.

The project uses:

```python
random.shuffle()
```

to randomly rearrange the questions before each quiz round.

A copy of the original question bank is created before shuffling. This prevents the original question list from being permanently modified.

Because the question bank contains more questions than are used in one round, the program selects only the required number after shuffling. Therefore, both the order and selection of questions can vary between different games.

---

# ✨ Features Implemented

## 1. Question Bank

The application contains a collection of **15 multiple-choice Python questions**.

Each question is represented using a dictionary containing:

- Question text
- Four answer choices
- Correct answer

The questions cover fundamental Python topics such as:

- Operators
- Data types
- Functions
- Loops
- Conditional statements
- Comments
- Lists
- File handling
- Exception handling

---

## 2. Randomized Questions

At the beginning of every quiz round, the question bank is copied and shuffled.

The game then selects **10 questions** from the shuffled list.

This means that the user does not receive exactly the same questions in the same order every time they play.

---

## 3. Question Display and Input Validation

Questions are presented one at a time with four choices labeled:

```text
A
B
C
D
```

The user must enter one of these four letters.

The program accepts both uppercase and lowercase input.

For example:

```text
A
a
```

are both accepted.

If an invalid value is entered, the program displays an error message and asks the user again instead of crashing or moving to the next question.

---

## 4. Immediate Feedback

After every answer, the program immediately informs the user whether the answer was correct.

If the answer is incorrect, the program also displays:

- The correct answer letter
- The complete correct option

This allows the player to learn from mistakes immediately.

---

## 5. Score Calculation

The program maintains a running score throughout the quiz.

After all 10 questions have been answered, it calculates:

- Number of correct answers
- Total questions
- Percentage
- Letter grade

The grading system is:

| Percentage | Grade |
|------------|-------|
| 90% or above | A |
| 80%–89% | B |
| 70%–79% | C |
| 60%–69% | D |
| Below 60% | F |

Each grade is accompanied by a suitable feedback message.

---

## 6. High Score Tracking

The application keeps track of the highest score achieved.

The high score is stored in:

```text
highscore.txt
```

When the program starts, it reads the previous high score from the file.

If the player achieves a score higher than the stored score, the application:

1. Displays a **New High Score** message.
2. Saves the new score to the file.

If the score does not exceed the existing record, the saved high score remains unchanged.

The program also handles the first run when `highscore.txt` does not yet exist.

---

## 7. Play Again

After completing a quiz round, the user is asked whether they want to play again.

The program accepts:

```text
yes
y
```

to start another round.

A new round is created with a newly shuffled set of questions.

The user can continue playing multiple rounds until they choose to stop.

---

## 8. Input Validation

Input validation is included throughout the application.

The program checks:

- Quiz answers
- Play-again responses
- High-score file contents

Invalid answers do not cause the application to terminate unexpectedly. Instead, the user is prompted to provide valid input.

---

# 🧩 Program Structure

The application is divided into separate functions so that each part of the program has a clear responsibility.

### `ask_question()`

Displays a question and its options, validates the user's answer, and determines whether the answer is correct.

### `get_grade()`

Calculates the percentage and determines the appropriate letter grade and feedback message.

### `show_results()`

Displays the final quiz results, including score, percentage, grade, and feedback.

### `load_high_score()`

Reads the saved high score from `highscore.txt`. If the file is missing or contains invalid data, the program uses zero as the starting high score.

### `save_high_score()`

Writes a new high score to the text file.

### `play_quiz()`

Controls a complete quiz round. It shuffles the questions, selects 10 questions, asks them one by one, keeps track of the score, and displays the final results.

### `play_again()`

Checks whether the user wants to start another quiz round.

### `main()`

Controls the overall application flow and continues running the game until the user decides to exit.

---

# ▶️ How to Run

Make sure **Python 3.x** is installed.

No external packages are required because the project uses Python's standard library.

### Step 1

Download or clone the project repository.

### Step 2

Open the project folder in an editor such as:

- Visual Studio Code
- IDLE
- PyCharm

### Step 3

Run:

```bash
python quiz_game.py
```

### Step 4

Press Enter to begin the quiz.

Answer each question using:

```text
A
B
C
D
```

After the quiz ends, review the results and choose whether to play another round.

---

# 📸 Screenshots

The repository contains screenshots demonstrating the main parts of the application:

- Starting screen
- Current high score
- Question with answer choices
- Correct answer feedback
- Incorrect answer feedback
- Final results
- Grade and percentage
- New high score message
- Play-again prompt

Recommended screenshot files:

```text
screenshots/
├── start_screen.png
├── question.png
└── results.png
```

---

# 🛠️ Challenges Faced and Solutions

### Challenge 1 — Keeping the Original Question Bank Unchanged

Using `random.shuffle()` directly on the main question list would change its order permanently.

To avoid this, a copy of the question bank is created first:

```python
questions = QUESTIONS.copy()
random.shuffle(questions)
```

The shuffled copy is used for the current round while the original question bank remains unchanged.

---

### Challenge 2 — Handling a Missing High-Score File

When the application is run for the first time, `highscore.txt` may not exist.

Trying to read a missing file could cause an error.

This was handled using `try` and `except`, allowing the program to start with a high score of zero when the file is unavailable.

---

### Challenge 3 — Validating Quiz Answers

The program needs to make sure the user enters only `A`, `B`, `C`, or `D`.

A `while` loop is used so the program continues asking until a valid answer is provided.

The `upper()` string method also allows lowercase answers to work correctly.

---

### Challenge 4 — Maintaining the High Score

The high score needs to remain available between different program sessions.

This was solved by storing the highest score in `highscore.txt` and loading it again when the application starts.

---

# 📚 What I Learned

This project helped me understand how the `random` module can be used to introduce randomness into a Python program.

I also strengthened my understanding of:

- Functions
- Loops
- Conditional statements
- Lists
- Dictionaries
- File handling
- Exception handling
- Input validation
- String methods
- Randomization
- Program control flow

The project also helped me understand how smaller functions can be combined to create a complete application instead of placing all program logic in one large block of code.

---

# 🚀 Future Improvements

If I had more time, I would consider adding:

- Grade letters alongside individual question scores
- Subject/category-based questions
- Different difficulty levels
- A larger question bank
- Individual player names
- A leaderboard
- A formatted report file
- A timer for each question
- More detailed statistics

---

# 📁 Repository Contents

```text
CloudExify-Project-3/
│
├── quiz_game.py
├── highscore.txt
├── README.md
└── screenshots/
    ├── start_screen.png
    ├── question.png
    └── results.png
```

### `quiz_game.py`

Contains the complete Python quiz application, including the question bank, quiz logic, scoring, grading, randomization, validation, and high-score management.

### `highscore.txt`

Stores the highest score achieved by the player and is automatically created or updated by the application.

### `README.md`

Contains the project description, implemented features, instructions, challenges, learning outcomes, and future improvements.

### `screenshots/`

Contains screenshots demonstrating the working application.

---

# ✅ Conclusion

The Python Quiz Game combines several fundamental Python concepts into one interactive command-line application.

The project provided practical experience with randomization, user input, validation, scoring, file persistence, and program structure while reinforcing concepts learned during the previous projects.

It also provided a useful introduction to designing an application around user interaction and maintaining data between different sessions.

---

**CloudExify Python Internship 2026**  
**Month 2 — Project 3**  
**Muhammad Anees**  
**CX-INT-2026-PY-0303**