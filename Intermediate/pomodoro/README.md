# Pomodoro Timer: A Python Tkinter Application
![Pomodoro Timer](https://github.com/MogharedWahid/PythonPlayground/blob/main/Intermediate/pomodoro/pomodoro.png)
The Pomodoro Timer is a simple desktop application built using Python and Tkinter. This application implements the **Pomodoro Technique**, a time management method that uses intervals of focused work followed by short breaks. After completing four Pomodoro cycles, a longer break is taken. The goal of this timer is to improve productivity by breaking work into manageable chunks and providing regular rest periods.

## Features

- **Work Sessions**: 25 minutes of focused work time.
- **Short Breaks**: 5-minute breaks between work sessions to relax and recharge.
- **Long Breaks**: After completing four Pomodoro cycles, take a longer 20-minute break.
- **Visual Timer**: A countdown timer displayed on the main window, indicating the remaining time in the current session.
- **Session Tracking**: Displays checkmarks to indicate how many Pomodoro cycles have been completed.
- **Simple and Intuitive Interface**: A user-friendly interface to easily start, reset, and monitor the timer.

## Requirements

- Python 3.x installed on your system.
- Tkinter (usually comes pre-installed with Python).

## How to Use

1. **Start a Pomodoro Cycle:**
    * Click the Start button to begin the timer. The timer will begin a 25-minute work session.

2. **Break Periods:**
    * After each work session (25 minutes), a 5-minute short break will start automatically.
    * After completing four Pomodoro cycles (4 work sessions), a 20-minute long break will start.

3. **Session Completion:**
    * Once a session is completed (either work or break), a checkmark is displayed to track your progress. For every 2 completed work sessions, the checkmark count increases by 1.

4. **Resetting the Timer:**
    * You can reset the timer at any point by clicking the Reset button. This will cancel the current countdown, set the timer back to 00:00, and reset the session counter.

## Code Structure
The code consists of the following main components:

### 1. Constants
The following constants define the time durations for the work sessions and breaks:
  * `WORK_MIN = 25`: Duration for a work session in minutes.
  * `WORK_SEC`: Work session duration in seconds (`WORK_MIN * 60`).
  * `SHORT_BREAK_MIN = 5`: Duration for a short break in minutes.
  * `SHORT_BREAK_SEC`: Short break duration in seconds (`SHORT_BREAK_MIN * 60`).
  * `LONG_BREAK_MIN = 20`: Duration for a long break in minutes.
  * `LONG_BREAK_SEC`: Long break duration in seconds (`LONG_BREAK_MIN * 60`).

### 2. Functions
  * `reset_timer()`: Resets the timer and clears any checkmarks or session progress.
  * `start_timer()`: Starts the timer for the next session (work or break). The function also handles the logic for switching between work sessions, short breaks, and long breaks.
  * `count_down(count)`: The countdown function updates the timer display every second. Once the timer reaches 0, it calls the `start_timer()` function to initiate the next session.

### 3. User Interface
  * **Main Window**: The main window is created using Tkinter's `Tk()` class, and it is configured with padding and background color.
  * **Canvas**: The canvas is used to display the tomato image and the countdown timer.
  * **Buttons**: Two buttons, Start and Reset, are provided to control the timer.
  * **Labels**: Labels are used to display the current session ("Work", "Break") and checkmarks.
### 4. Main Loop
  * The Tkinter event loop (`window.mainloop()`) is used to keep the application running and responding to user actions.

## Customization
You can easily modify the application to suit your needs by adjusting the following variables:
  * `WORK_MIN`, `SHORT_BREAK_MIN`, and `LONG_BREAK_MIN` to change the duration of the work sessions and breaks.
  * The colors (`PINK`, `RED`, `GREEN`, `YELLOW`) can be changed to customize the look and feel of the app.
  * Replace the `tomato.png` image with your custom image for the timer background (ensure it’s in the same directory).
