# Turtle Crossing Game
![Turtle Crossing Game](https://github.com/MogharedWahid/PythonPlayground/blob/main/Intermediate/turtle_crossing_game/Turtle_Crossing.jpg)

Welcome to the Turtle Crossing Game! This project is a fun and interactive game where players control a turtle attempting to cross a busy road filled with moving cars. The game is developed using Python's Turtle graphics library, which provides a simple way to create graphics and animations.

## Table of Contents

- [Overview](#overview)
- [Gameplay Instructions](#gameplay-instructions)
- [Features](#features)
- [Project Structure](#project-structure)
- [Future Enhancements](#future-enhancements)

## Overview

The Turtle Crossing Game is inspired by classic arcade games where the player must navigate a character across a series of obstacles. In this game, you control a turtle that must cross a road filled with cars moving at varying speeds. The objective is to reach the top of the screen without getting hit by a car. Each successful crossing increases the level, making the game progressively more challenging.

## Gameplay Instructions
* **Objective:** Guide the turtle to the top of the screen without colliding with any cars.
* **Controls:** Use the Up Arrow key to move the turtle forward.
* **Level Progression:** Each time the turtle successfully crosses the road, the level increases, and the cars move faster.
* **Game Over:** If the turtle collides with a car, the game ends, and a "GAME OVER" message is displayed.

## Features
* **Dynamic Difficulty:** The game becomes more challenging as the player progresses through levels.
* **Randomized Car Generation:** Cars are generated with random colors and positions, ensuring a unique experience each time.
* **Simple and Intuitive Controls:** The game is easy to play with straightforward controls.
* **Visual Feedback:** The current level is displayed on the screen, providing feedback on the player's progress.

## Project Structure
* **`main.py`:** The entry point of the game. It sets up the game environment, handles the game loop, and manages interactions between different components.
* **`player.py`:** Contains the `Player` class, which manages the turtle's movement and position.
* **`car_manager.py`:** Contains the `CarManager` class, responsible for creating and moving cars across the screen.
* **`scoreboard.py`:** Contains the `Scoreboard` class, which displays the current level and game over message.

## Future Enhancements
* **Additional Levels:** Introduce new levels with different challenges and obstacles.
* **Power-Ups:** Add power-ups that provide temporary advantages, such as slowing down cars or granting invincibility.
* **Sound Effects:** Incorporate sound effects to enhance the gaming experience.
* **Multiplayer Mode:** Allow multiple players to compete or cooperate in crossing the road.
