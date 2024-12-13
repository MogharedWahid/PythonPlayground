# Spot Painting
![Spot Painting](https://github.com/MogharedWahid/PythonPlayground/blob/main/Intermediate/spot_painting/image.jpg)

This project uses Python's `turtle` module to create a beautiful grid of dots where the colors of the dots are extracted from an image using the `colorgram` module. The program paints a grid of circles with random colors extracted from a given image, creating a dynamic and colorful pattern.

## Features
- Extracts a set of colors from an image.
- Generates a grid of colored dots on the screen.
- The grid is dynamically centered within the window.
- The window is maximized for a better user experience.

## Libraries Used
- **Turtle Graphics**: A Python library for simple drawing and graphics.
- **Colorgram**: A Python library to extract colors from an image.
- **Random**: Standard Python library for generating random values.

## Setup and Installation
You will need the following Python libraries:
1. `turtle` (part of Python’s standard library, no installation required)
2. `colorgram` (for extracting colors from an image)

You can install `colorgram` using pip:
```bash
pip install colorgram.py
```

## Files
* `image.jpg`: The image file from which the colors are extracted (should be placed in the same directory as the Python script).
* `spot_painting.py`: The Python script that generates the painting.

## Usage
1. Place your image file (image.jpg) in the same directory as the Python script.
2. Run the Python script:
```bash
python turtle_painting.py
```
3. The program will start drawing a grid of dots on the turtle graphics window. The colors used for the dots will be randomly selected from the extracted colors of the image.
4. The turtle window will remain open until you click on it to close.

## How It Works
**Step 1: Color Extraction**

The script uses the `colorgram` module to extract up to 30 prominent colors from the image file (`image.jpg`). These colors are stored as RGB tuples.

**Step 2: Drawing the Grid**

The turtle starts at the top-left corner of the screen and begins drawing a grid of dots. Each dot is 20 pixels in size and filled with a random color from the list of extracted colors.

**Step 3: Centering the Grid**

The grid of dots is centered in the window using calculations based on the size of the grid and the turtle's starting position.
