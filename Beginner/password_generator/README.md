# PyPassword Generator

Welcome to the **PyPassword Generator**! This is a simple command-line tool that allows users to generate random passwords based on their specifications, including letters, symbols, and numbers. The generated passwords can be in an easy-to-read format or a more secure random order.

## Features

- Generate random passwords containing:
  - Uppercase and lowercase letters
  - Numbers
  - Special characters (symbols)
- Choose the number of letters, symbols, and numbers for your password
- Two password generation modes:
  - **Easy Version**: Outputs the password in a sequential manner (letters, symbols, numbers)
  - **Hard Version**: Outputs a randomized password that mixes all character types

## Requirements

- Python 3.x

## How to Use

1. **Clone the repository**:
   ```bash
   git clone https://github.com/MogharedWahid/PythonPlayground.git
   cd PythonPlayground/password_generator
2. **Run the Password Generator**: Open a terminal and run the following command:
   ```bash
   python password_generator.py
3. **Input your preferences**:
    * You will be prompted to enter the number of letters, symbols, and numbers you would like in your password.
    * For example:
    ```sql
    How many letters would you like in your password?
    How many symbols would you like?
    How many numbers would you like?
    ```
4. **View your generated password**:
    * The program will display both the easy version and the hard version of your generated password.

## Example
Here’s an example of what the output might look like:
```vbnet
Welcome to the PyPassword Generator!
How many letters would you like in your password?
3
How many symbols would you like?
2
How many numbers would you like?
1
Your password is: abc$#1 (easy version)
Your password is: a1$bc (hard version)
```

## Code Explanation
* The code starts by importing the random module and defining lists of characters (letters, numbers, and symbols).
* It prompts the user to specify how many of each character type to include in the password.
* The program generates the password in two versions:
  * The easy version outputs the characters in the order specified.
  * The hard version shuffles the characters for enhanced security.
