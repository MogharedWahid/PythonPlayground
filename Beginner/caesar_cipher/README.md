# Caesar Cipher

![Caesar Cipher Logo](https://github.com/MogharedWahid/PythonPlayground/blob/main/Beginner/caesar_cipher/caesar_cipher.jpg)

Welcome to the Caesar Cipher project! This project implements a simple Caesar cipher, a type of substitution cipher where each letter in the plaintext is 'shifted' a certain number of places down or up the alphabet.

## Features

- Encode and decode messages using a user-defined shift value.
- Supports both uppercase and lowercase letters.
- Handles non-alphabetic characters gracefully by leaving them unchanged.
- Interactive command-line interface for user inputs.

## Getting Started

To get a copy of this project up and running on your local machine, follow these simple steps:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/MogharedWahid/PythonPlayground.git
   cd PythonPlayground/caesar_cipher
  
2. **Run the game:**

  ```bash
  python caesar_cipher.py
  ```

## Usage
1. Choose to "encode" or "decode" a message.
2. Enter your message.
3. Specify a shift number (an integer).
4. The program will output the encoded or decoded message.

## How It Works
The Caesar cipher works by shifting the letters of the alphabet by a specified number. For example, with a shift of 3, 'A' becomes 'D', 'B' becomes 'E', and so on. When decoding, the letters are shifted back by the same amount.
**Example:**
  * Encoding: "hello" with a shift of 3 becomes "khoor"
  * Decoding: "khoor" with a shift of 3 returns to "hello"

## Modules
This project includes the following modules:
* caesar_cipher.py: The main logic that handles the encoding, decoding and user inputs.
* art.py: Contains ASCII art for the logo of the game.

  
