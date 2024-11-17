# Rock-Paper-Scissors Game

Welcome to the **Rock-Paper-Scissors** game! This is a simple command-line game where you can compete against the computer. The game features ASCII art for visual representation and allows you to play multiple rounds.

## Table of Contents
- [Features](#features)
- [Requirements](#requirements)
- [How to Run the Game](#how-to-run-the-game)
- [Gameplay Instructions](#gameplay-instructions)
- [Game Logic](#game-logic)
- [ASCII Art](#ascii-art)
- [License](#license)

## Features
- Play against a computer opponent.
- Clear ASCII art representations of Rock, Paper, and Scissors.
- Friendly user prompts and feedback for game results.

## Requirements
- Python 3

## How to Run the Game
1. Clone the repository:
   ```bash
   git clone https://github.com/MogharedWahid/PythonPlayground.git
2. Navigate to the project directory:
   ```bash
   cd PythonPlayground
3. Run the game:
   ```bash
   python rock_paper_scissors/rock_paper_scissors.py

## Gameplay Instructions
When prompted, enter 0, 1, or 2 to choose Rock, Paper, or Scissors, respectively.
The computer will make a random choice.
The result will be displayed, along with ASCII art representations of the choices made.
After each round, you can choose to play again or exit the game.

## Game Logic
* Winning Conditions:
  * Rock crushes Scissors (Rock wins)
  * Scissors cuts Paper (Scissors wins)
  * Paper covers Rock (Paper wins)
* If both players choose the same option, the game is a draw.

## ASCII Art
The game includes ASCII art for each choice:
* Rock:
```scss
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
```
* Paper:
```scss
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
```
* Scissors:
```scss
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)



