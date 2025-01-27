# Flash Card App
![Flash Card App](https://github.com/MogharedWahid/PythonPlayground/blob/main/Intermediate/flash_card_app/images/Flashy.jpg)

Flashy is a simple flashcard application built using Python and Tkinter. It allows users to learn and memorize new words, particularly German-English vocabulary, by showing the German word and revealing the English translation after a few seconds. Users can mark a word as "known" by clicking a button, which removes it from the list of words to learn.

## Features

- Displays a random German word on the front of the card.
- After 3 seconds, flips the card to reveal the English translation.
- Allows users to mark words they know, removing them from the learning list.
- Saves progress by updating the list of words to learn in a CSV file.

## Requirements

- Python 3.x
- Tkinter (for GUI)
- pandas (for CSV file handling)

You can install the required libraries using the following command:
  ```
  pip install pandas
  ```
    
### Note:
Tkinter should be included with the standard Python installation. If you don't have it, you may need to install it separately depending on your operating system.

## File Structure
```bash
flash_card_app/
│
├── data/
│   ├── words_to_learn.csv       # Holds words that need to be learned
│   └── german_words.csv         # Default list of words (if words_to_learn.csv is missing)
│
├── images/
│   ├── card_front.png           # Front image of the flashcard
│   ├── card_back.png            # Back image of the flashcard
│   ├── right.png                # Image for the "known" button
│   └── wrong.png                # Image for the "unknown" button
│
├── main.py                      # Main Python script
└── README.md                    # Documentation
```

## How It Works
**1. Starting the Application:** When you run `main.py`, the application loads either a list of words to learn (from `words_to_learn.csv`) or, if that file is missing, it falls back to a default CSV file (`german_words.csv`).

**2. Displaying Flashcards:** The main window displays a flashcard with a German word. After 3 seconds, the card flips to show the English translation.

**3. Marking Words as Known:** If you know a word, click the checkmark button to remove it from the list. The list of words to learn is saved to `words_to_learn.csv` to keep track of your progress.

**4. Navigation:** If you don’t know a word, click the cross button to get the next word in the list.

## How to Use
1. Clone or download the project.

2. Install the required Python libraries.

3. Ensure the `data/words_to_learn.csv` or `data/german_words.csv` file is available.

4. Run the `main.py` script:
    ```
    python main.py
    ```
5. Use the "Check" button to mark words as known and the "Cross" button to move to the next word.

## Customization
* You can modify the data/german_words.csv file to add your own words.
* Replace the images in the images/ directory to customize the appearance of the flashcards.

## Troubleshooting
* FileNotFoundError: If the `words_to_learn.csv` file does not exist, the app will use `german_words.csv` by default. Make sure the `data/` directory contains one of these files.
* Tkinter Not Installed: If Tkinter is not installed, you can install it based on your operating system:
  * On Windows, Tkinter is usually pre-installed with Python.
  * On Ubuntu, you can install it with sudo `apt-get install python3-tk`.
