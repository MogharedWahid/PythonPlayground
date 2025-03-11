# Quizzler - A True/False Quiz Application
![Quizzler GUI App](https://github.com/MogharedWahid/PythonPlayground/blob/main/Intermediate/quizzler/quizzler.jpg)

This project is a Python-based True/False quiz application that utilizes the Open Trivia Database API to fetch questions and provides a graphical user interface (GUI) using Tkinter.

## Features

* Fetches True/False questions from the Open Trivia Database API.
* Presents questions in a user-friendly GUI.
* Tracks and displays the user's score.
* Provides visual feedback for correct and incorrect answers.
* Displays the final score upon completion of the quiz.

## Files Description

* `question_model.py`: Defines the `Question` class, which represents a single quiz question with its text and answer.
* `quiz_brain.py`: Implements the `QuizBrain` class, which manages the quiz logic, including question tracking, score calculation, and answer checking.
* `data.py`: Fetches question data from the Open Trivia Database API and stores it in a list.
* `ui.py`: Creates the graphical user interface using Tkinter and handles user interactions.
* `main.py`: Orchestrates the application by creating question objects, initializing the quiz brain, and starting the GUI.

## How It Works

1.  **Data Fetching:**
    * The `data.py` file uses the `requests` library to fetch True/False questions from the Open Trivia Database API.
    * The fetched data is parsed from JSON and stored in a list.
2.  **Question Model:**
    * The `question_model.py` file defines the `Question` class, which holds the text and correct answer for each question.
3.  **Quiz Logic:**
    * The `quiz_brain.py` file manages the quiz flow:
        * It tracks the current question number and the user's score.
        * It retrieves questions from the list and checks user answers.
        * It uses the html library to unescape html characters.
4.  **User Interface:**
    * The `ui.py` file creates the GUI using Tkinter:
        * It displays questions on a canvas.
        * It provides True and False buttons for user input.
        * It shows the user's score.
        * It gives visual feedback (green for correct, red for incorrect).
5.  **Main Application:**
    * The `main.py` file brings everything together:
        * It creates `Question` objects from the fetched data.
        * It initializes a `QuizBrain` instance.
        * It creates a `QuizInterface` instance to start the GUI.

## Technologies Used

* Python
* Tkinter (GUI)
* Requests (HTTP requests)
* Open Trivia Database API

## Setup and Installation

1.  **Clone the repository:**
2.  **Install the required libraries:**
    ```bash
    pip install requests
    ```
3.  **Run the application:**
    ```bash
    python main.py
    ```
4.  **Images:**
    * Place the true.png, and false.png images inside of a folder called images in the same directory as the python files.

## Future Enhancements

* Implement different question categories and difficulty levels.
* Add a timer for each question.
* Improve the GUI design and user experience.
* Add more robust error handling.
* Add a high score tracking system.
