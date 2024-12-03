# Blackjack Game

![Blackjack Logo](https://github.com/MogharedWahid/PythonPlayground/blob/main/Beginner/blackjack/blackjack.jpg)

Welcome to the **Blackjack Game**! This is a Python implementation of the classic card game, where players compete against a computer dealer. The goal is to accumulate a higher score than the dealer without exceeding 21.

## Features

- Play against a computer dealer.
- Easy-to-use command-line interface.
- Handles special cases like Blackjack and busts automatically.
- Keeps track of scores and determines the winner.

## Getting Started

### Prerequisites

Ensure you have Python 3.x installed on your computer. You can download it from [python.org](https://www.python.org/downloads/).

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/MogharedWahid/PythonPlayground.git
2. Running the Game:
   ```bash
   cd PythonPlayground/blackjack
   python blackjack.py
   ```

### How to Play
1. **Start the Game:** The game begins by dealing two cards to both you and the dealer.
2. **Decide Your Move:** You can choose to draw another card (hit) or keep your current total (stand).
3. **Watch the Dealer:** The dealer will draw cards until their score is 17 or higher.
4. **Winning the Game:** The player with a score closest to 21 without exceeding it wins.

### Game Rules
  * The game uses a standard deck of cards.
  * Number cards are worth their face value.
  * Kings, Queens, and Jacks are worth 10 points.
  * Aces can be worth 1 or 11 points, depending on which value benefits the hand more.
  * If you achieve a score of 21 with your first two cards, it's called a Blackjack, and you win instantly (unless the dealer also has Blackjack, which results in a draw).

### Game Logic
  * If your score exceeds 21, you "bust" and lose the game.
  * If both you and the dealer have the same score, the game is a draw.
  * If the dealer busts, you win automatically.
  * The dealer must draw cards until their score is 17 or higher.


