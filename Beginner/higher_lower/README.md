# Higher Lower Game

![Higher Lower Game Logo](https://github.com/MogharedWahid/PythonPlayground/blob/main/Beginner/higher_lower/higher_lower.png)

Welcome to the Higher Lower Game! This interactive console-based game allows players to guess which celebritys or influencers has higher or lower followers on Instagram. The game randomly selects two influencers from a dataset and challenges the player to determine which one has a higher follower count.

## Game Overview

In this game, players are presented with two different influencers, each accompanied by their descriptions and countries of origin. The goal is to identify which influencer has a greater number of Instagram followers. Correct guesses earn points, and the game continues until the player makes an incorrect guess.

## Features

- **Random Comparisons**: Each round features a random selection of two influencers.
- **Score Tracking**: Players earn points for correct answers.
- **Immediate Feedback**: Players receive instant notifications about the correctness of their guesses.
- **User-Friendly Interface**: The game is played in a simple console interface.

## Getting Started

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/MogharedWahid/PythonPlayground.git
2. Navigate to the project directory:
   ```bash
   cd PythonPlayground/higher_lower
3. Ensure you have the required files:
    * art.py: This file contains the ASCII art for the game logo and the "versus" graphic.
    * game_data.py: This file contains the dataset with information about various influencers on Instagram, including their follower counts.

## How to Play
1. **Run the game script:**
  ```bash
  python game.py
  ```

2. **Follow the on-screen prompts:**
    * Guess which influencer has more Instagram followers by typing 'A' or 'B'.
3. **Receive immediate feedback** on your answer and track your score.

## Game Data
The game relies on a dataset stored in game_data.py. Each influencer should be represented as a dictionary with the following keys:
  * name: The name of the influencer.
  * description: A brief description of the influencer.
  * country: The country of the influencer.
  * follower_count: The number of Instagram followers.
Ensure your dataset is accurate and up-to-date for the best gameplay experience.

