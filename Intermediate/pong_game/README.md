# Pong Game
![Pong Game](https://github.com/MogharedWahid/PythonPlayground/blob/main/Intermediate/pong_game/pong.jpg)

This is a classic **Pong** game implemented in Python using the `turtle` module. It allows two players to control paddles and try to score by bouncing a ball back and forth. The game features basic paddle control, scoring, and simple ball physics.

## Features
- **Two-player mode**: Play against a friend on the same machine.
- **Ball bounce mechanics**: The ball bounces off paddles and walls.
- **Dynamic scoring**: Tracks the score for both players in real-time.
- **Responsive controls**: Move the paddles up and down using the keyboard.

## Controls
- **Right Paddle**: 
  - Up Arrow Key: Move the paddle up
  - Down Arrow Key: Move the paddle down
- **Left Paddle**: 
  - 'W' Key: Move the paddle up
  - 'S' Key: Move the paddle down

## How the Game Works
1. The game is played with two paddles and a ball.
2. Each player controls a paddle using the arrow keys (right paddle) or w and s keys (left paddle).
3. The ball bounces off the top and bottom walls, and players bounce the ball back and forth using their paddles.
4. When the ball passes a paddle, the opponent scores a point, and the ball resets to the center.
5. The game keeps track of the score for both players and updates the scoreboard in real-time.

## Project Structure
This project consists of the following files:
* **main.py:** The main game logic, where the game loop runs and user inputs are handled.
* **paddle.py:** Contains the Paddle class for creating and controlling the paddles.
* **ball.py:** Contains the Ball class, which handles the ball's movement and interaction with the paddles and walls.
* **scoreboard.py:** Manages the score display and keeps track of the scores for both players.

## Enhancements and Future Improvements
Here are some potential features to enhance the game:
* **AI Player:** Add an AI-controlled paddle to play against the computer.
* **Power-ups:** Introduce power-ups like ball speed boosts or larger paddles.
* **Sound Effects:** Add sound effects for ball bounces and score events.
* **Game Over Screen:** Display a "Game Over" message once a player reaches a certain score.
* **Multiple Difficulty Levels:** Adjust ball speed and paddle sizes for different difficulty levels.
* **Pause Feature:** Allow the game to be paused with a specific key press.
* 
