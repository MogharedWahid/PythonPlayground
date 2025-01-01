# Snake Game II
![Snake Game](https://github.com/MogharedWahid/PythonPlayground/blob/main/Intermediate/snake_game_II/snake-game.jpg)

Welcome to the Snake Game, a classic arcade game implemented in Python using the Turtle graphics library. This project is a fun way to practice Python programming and understand basic game development concepts.

## Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [How to Play](#how-to-play)
- [Game Mechanics](#game-mechanics)

## Features

- **Interactive Gameplay:** Control the snake using keyboard arrow keys.
- **Dynamic Growth:** The snake grows longer each time it eats the food.
- **Score Tracking:** Keep track of your current score and high score.
- **Collision Detection:** The game resets if the snake collides with the wall or its own tail.
- **Persistent High Score:** The high score is saved between sessions.

## Project Structure
```
Snake-Game/
│
├── snake.py            # Snake class
├── food.py             # Food class
├── scoreboard.py       # Scoreboard class
├── main.py             # Main game loop
└── README.md           # Project documentation
└── data.txt            # File storing the high score
```

## How to Play

1. **Run the game:**
   
    Execute the following command in your terminal:
```
python main.py
```
2. **Control the Snake:**
   
    Use the arrow keys on your keyboard to navigate the snake:
* **Up Arrow:** Move up
* **Down Arrow:** Move down
* **Left Arrow:** Move left
* **Right Arrow:** Move right
  
3. **Objective:**
   
    Guide the snake to eat the food that appears randomly on the screen. Each time the snake eats the food, it grows longer, and your score increases.

## Game Mechanics
* **Food Collision:** When the snake's head is close to the food, the food is repositioned, the snake grows, and the score increases.
* **Wall Collision:** If the snake's head touches the boundary of the screen, the game resets, and the score is compared to the high score.
* **Tail Collision:** If the snake's head collides with any part of its body, the game resets.
