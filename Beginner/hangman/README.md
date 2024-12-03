# Hangman Game

![Hangman Logo](https://github.com/MogharedWahid/PythonPlayground/blob/main/Beginner/hangman/hangman.png)

Welcome to the Hangman Game! This is a simple yet fun command-line game implemented in Python where players guess letters to reveal a hidden word. The player has a limited number of incorrect guesses (lives) before losing the game.

## Features

- Randomly selects a word from a predefined list.
- User-friendly interface with clear prompts and instructions.
- Visual representation of the hangman state for each incorrect guess.
- Keeps track of correctly guessed letters and remaining lives.

## Installation

To run the Hangman game locally, follow these steps:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/MogharedWahid/PythonPlayground.git
   cd PythonPlayground/hangman
  
2. **Run the game:**

  ```bash
  python hangman.py
  ```

## Usage
1. Upon running the game, a logo will be displayed along with the instructions.
2. You will be prompted to guess letters one at a time.
3. The current state of the word will be displayed with underscores for unguessed letters.
4. You have 6 lives. Incorrect guesses will reduce your lives by one.
5. The game ends when you either guess the word or run out of lives.


## Modules
This project includes the following modules:
* hangman.py: The main game logic that handles the gameplay, user input, and the hangman stages.
* hangman_words.py: Contains a list of words that the game randomly selects for the player to guess.
* hangman_art.py: Contains ASCII art for the hangman stages and the logo for the game.

  

