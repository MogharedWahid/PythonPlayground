# Kanye Quote App
![Kanye Quotes App](https://github.com/MogharedWahid/PythonPlayground/blob/main/Intermediate/kanye_quote/KanyeQuote.jpg)

## Description
The Kanye Quotes App is a simple Python application built using the Tkinter library. It fetches random quotes from the Kanye West API and displays them in a graphical user interface (GUI). This project demonstrates the integration of web APIs with a desktop application, showcasing skills in Python programming and GUI development.

## Features
- Fetches and displays random quotes from the Kanye West API.
- User-friendly interface with a button to get new quotes.
- Customizable GUI elements (background and button images).

## Code Structure
- **Main Application File**: 
  - `main.py`: The main script that contains the application logic.
  
### Key Components
1. **Imports**:
   - `from tkinter import *`: Imports the Tkinter library for creating the GUI.
   - `import requests`: Imports the requests library for making HTTP requests to the API.

2. **Functionality**:
   - `get_quote()`: This function sends a GET request to the Kanye West API and updates the displayed quote on the canvas.

3. **GUI Setup**:
   - **Window**: A Tkinter window is created with specific dimensions and padding.
   - **Canvas**: A canvas is used as the main area for displaying the background image and quote text.
   - **Quote Text**: A text item is created on the canvas to display the quote, and its ID is stored for later updates.
   - **Button**: A button is added that triggers the `get_quote()` function when clicked.

## Tools Used
- **Python**: The programming language used to write the application.
- **Tkinter**: A built-in library in Python for creating graphical user interfaces.
- **Requests**: A popular external library used for making HTTP requests to access APIs.

## Conclusion
This project is a practical demonstration of using Python for GUI development and API integration. It serves as a foundation for further exploration into building more complex applications and working with external data sources.
