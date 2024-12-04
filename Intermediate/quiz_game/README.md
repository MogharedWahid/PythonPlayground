# Quiz Game

This project is a simple command-line quiz game built using Python. It is designed to practice Object-Oriented Programming (OOP) concepts, such as classes, objects, and methods. The quiz presents true/false questions, tracks the score, and provides feedback to the user.

## Features
- **True/False Questions**: The game asks true/false questions to the player.
- **Score Tracking**: The score is updated after each question based on user input.
- **Feedback**: After each answer, the game provides feedback on whether the user's answer was correct or not.
- **Final Score**: The game displays the final score once all questions have been answered.

## Project Structure

The project is divided into several files, each with a specific purpose:
```graphql
quiz_game/
│
├── data.py              # Contains question data
├── question_model.py    # Defines the Question class
├── quiz_brain.py        # Contains the QuizBrain class
└── main.py              # The main file that runs the game
```


### Files Overview

- **`data.py`**: Contains the question data. The questions are stored in a list of dictionaries, with each dictionary containing a question and its correct answer.
  
- **`question_model.py`**: Defines the `Question` class, which represents each individual question. Each `Question` object holds the question text and the correct answer.

- **`quiz_brain.py`**: Contains the `QuizBrain` class that controls the flow of the quiz. It checks if there are more questions, tracks the user's score, and evaluates their answers.

- **`main.py`**: The main file that runs the quiz. It initializes the game and interacts with the user.

## Classes

### `Question` Class
The `Question` class represents each quiz question and its corresponding correct answer.

**Attributes**:
- `text`: The text of the question.
- `answer`: The correct answer to the question (True/False).

### `QuizBrain` Class
The `QuizBrain` class handles the logic of the quiz game, including checking if there are more questions, evaluating answers, and updating the score.

**Methods**:
- `still_has_questions()`: Returns `True` if there are more questions to ask, otherwise returns `False`.
- `check_answer(user_answer, correct_answer)`: Compares the user's answer with the correct answer and updates the score.
- `next_question()`: Displays the next question and gets the user's input.

## How to Run the Game

1. Clone the repository to your local machine:
    ```bash
    git clone https://github.com/MogharedWahid/PythonPlayground.git
    ```

2. Navigate to the project directory:
    ```bash
    cd Intermediate/quiz_game
    ```

3. Run the `main.py` script to start the game:
    ```bash
    python main.py
    ```

The game will prompt you with a series of true/false questions. After you answer each question, it will provide feedback and update your score. Once all questions are answered, it will display your final score.


