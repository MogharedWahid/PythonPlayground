# Snake Game
![Snake Game](https://github.com/MogharedWahid/PythonPlayground/blob/main/Intermediate/snake_game/snake-game.jpg)

A simple Snake game built using Python's `turtle` graphics module. The game features a snake that the player can control using the arrow keys, with the goal of eating food to grow longer while avoiding collisions with the walls and the snake's own tail.

## Features

- **Snake Movement:** The snake moves in four directions (up, down, left, right) based on user input.
- **Snake Growth:** Each time the snake eats food, it grows in length.
- **Score Tracking:** The score is displayed at the top of the screen and increases each time the snake eats food.
- **Game Over Conditions:**
  - The game ends if the snake collides with the walls.
  - The game ends if the snake collides with its own body.
- **Food:** The food is placed randomly on the screen and is consumed by the snake to grow.

## Project Structure
```bash
snake-game/
│
├── main.py         # Main game file containing game loop and logic
├── food.py         # Class for managing food generation and collision
├── scoreboard.py   # Class for displaying score and game over message
└── snake.py        # Class for snake movement, growth, and collision
```

## Gameplay
* Control the snake:
  * Use the Up Arrow to move the snake up.
  * Use the Down Arrow to move the snake down.
  * Use the Left Arrow to move the snake left.
  * Use the Right Arrow to move the snake right.
* The goal is to eat the food, grow the snake, and avoid running into the walls or the snake’s body.
* When the game ends, the message "GAME OVER" will be displayed on the screen along with the final score.

## Code Explanation
### Snake Class (`snake.py`)
The `Snake` class is responsible for the snake's movement, growth, and direction:
* `__init__(self)`: Initializes the snake by creating a list of segments (`self.segments`) and calls the `create_snake()` method to initialize the snake with 3 segments. The head of the snake is assigned as `self.head`.
* `create_snake(self)`: Creates the initial snake, placing 3 segments at predefined positions. It uses the `add_segment()` method to add each segment to the `self.segments` list.
* `add_segment(self, position)`: Adds a new segment (represented as a `Turtle` object) to the snake at the specified position.
* `extend(self)`: Adds a new segment to the snake at the last segment's current position, used when the snake eats food.
* `move(self)`: Moves the snake forward by shifting each segment to the position of the segment ahead of it. The head of the snake moves forward by a fixed distance.
* Movement Methods (`up`, `down`, `left`, `right`): These methods control the snake’s direction, preventing the snake from turning directly back on itself.


### Food Class (`food.py`)
The `Food` class manages the food that the snake eats:
* `__init__(self)`: Initializes the food object with a circular shape, blue color, and positions it at a random location on the screen.
* `refresh(self)`: Generates new random x and y coordinates for the food within the game area and places the food there.


### Scoreboard Class (`scoreboard.py`)
The `Scoreboard` class tracks the score and displays it:
* `__init__(self)`: Initializes the scoreboard with a starting score of 0 and places the score at the top of the screen.
* `update_scoreboard(self)`: Displays the current score on the screen.
* `game_over(self)`: Displays the "GAME OVER" message and stops the game.
* `increase_score(self)`: Increases the score by 1 and updates the displayed score.


### Main Game Loop (`main.py`)
The main game loop controls the overall game flow:
* The game is displayed in a `turtle` screen of size 600x600 with a black background.
* The user controls the snake using the arrow keys.
* The game checks for collisions:
  * **Food Collision**: If the snake's head is close to the food, the snake grows, and the score increases.
  * **Wall Collision**: If the snake’s head crosses the screen boundaries, the game ends.
  * **Tail Collision**: If the snake’s head collides with any of its body segments, the game ends.
* The screen is updated every 0.1 seconds using `time.sleep(0.1)`.

