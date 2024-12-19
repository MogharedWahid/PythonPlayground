# Turtle Race Game
![Turtle Race](https://github.com/MogharedWahid/PythonPlayground/blob/main/Intermediate/turtle_race/turtle_race.jpg)

This is a simple Python Turtle Race game where the player can place a bet on which turtle will win the race. The game features six turtles of different colors, and the user can bet on their favorite turtle. The turtles move randomly, and the game will announce the winner based on the user's bet.

## Features

- **Betting System**: The player can input the color of the turtle they think will win.
- **Random Movement**: Each turtle moves a random distance in each iteration, simulating an unpredictable race.
- **Winner Announcement**: The game announces if the player won or lost based on the turtle's color.

## Requirements

- Python 3.x
- The `turtle` graphics library (which comes pre-installed with Python).

## How to Play

1. Clone the repository or download the Python file.
2. Run the Python script (`turtle_race.py`).
3. The game will prompt you to input a color for your bet.
4. Watch the race as the turtles move towards the finish line.
5. The game will announce if you won or lost based on your bet.

## How It Works
1. The game window will pop up with a prompt asking you to place a bet on which turtle (based on its color) will win the race.
2. The six turtles are placed at the starting line, and each turtle has a color (red, orange, yellow, green, blue, purple).
3. Each turtle moves forward randomly by a random number of steps (between 0 and 5).
4. The game ends when a turtle reaches the finish line (x-coordinate of 230 or greater).
5. If the turtle you bet on wins, the game will tell you that you won; otherwise, you lose.

## Example Output
```text
Make your bet: Which turtle will win the race? Enter a color: red

Race is starting...
YOU LOST 😭. The orange turtle won the race!
```
