# U.S. States Guessing Game
![U.S. states game](https://github.com/MogharedWahid/PythonPlayground/blob/main/Intermediate/unitesd_states_game/US_states.jpg)

Welcome to the U.S. States Guessing Game! This interactive game challenges users to name all 50 U.S. states. As you guess correctly, the state names are displayed on a map of the United States. This project is a fun way to test and improve your knowledge of U.S. geography.

## Features

- **Interactive Map**: A visual representation of the U.S. map where states are marked as you guess them.
- **User Input**: Prompts the user to enter state names.
- **Feedback**: Correct guesses are displayed on the map, providing immediate feedback.
- **Learning Tool**: If you choose to exit the game, a CSV file is generated with the states you have yet to guess, allowing you to focus your learning.

## Requirements

- **Python 3.x**: Ensure you have Python installed on your system.
- **pandas**: A powerful data manipulation library. Install it using pip if not already installed.
- **turtle**: A standard Python library for drawing graphics, included with Python.

## Installation

1. **Clone the Repository**:
2. **Install Required Packages**:

    Use pip to install the necessary Python packages:
    ```
    pip install pandas
    ```

## Usage
1. **Ensure Necessary Files**:

    * `50_states.csv`: This file should be in the project directory. It contains the state names and their corresponding x and y coordinates for placement on the map.
    * `blank_states_img.gif`: This image file serves as the background map for the game.

2. **Run the Game**:
    Execute the main script to start the game:
    ```
    python main.py
    ```

3. **Gameplay Instructions**:

    * You will be prompted to enter the name of a U.S. state.
    * If your guess is correct, the state name will appear on the map at its corresponding location.
    * The game continues until you have guessed all 50 states or choose to exit.
    * Type "Exit" to end the game early. A file named `states_to_learn.csv` will be created, listing the states you have not yet guessed.

## Files
* `main.py`: The main script that runs the game.
* `50_states.csv`: A CSV file containing the names and coordinates of the states.
* `blank_states_img.gif`: The image file used as the map background.
