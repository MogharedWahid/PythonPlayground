# Secret Auction Program

Welcome to the **Secret Auction Program**! This is a simple Python program that allows multiple users to place bids in a secret auction. After all bids are placed, the program identifies and announces the highest bidder.

## Features

- Allows multiple bidders to participate in an auction.
- Displays a logo and a welcome message.
- Accepts bids from users, associates them with their names.
- Determines and announces the winner, based on the highest bid.
- Clears the screen after each bid to keep the interface clean.

## Files in the Repository

- **main.py**: The main Python script for the secret auction program.
- **art.py**: Contains the ASCII art logo (used at the start of the auction).
  
## How to Use

1. **Clone the repository and run the program**:
   ```bash
   git clone https://github.com/MogharedWahid/PythonPlayground.git
   cd PythonPlayground/secret_auction
   python secret_auction.py
   ```
2. **Enter your bid:**
  * The program will prompt you to enter your name and your bid.
  * After entering your bid, it will ask if there are any other bidders.
  * The process will repeat until all bidders have placed their bids.

3. **Find out the winner:**
  * After the bidding is closed, the program will print the name of the highest bidder and the winning bid.

## Example
**Sample Input:**
```python
What is your name?: John
What is your bid?: $250
Are there any other bidders? Type 'yes' or 'no'.
yes
What is your name?: Alice
What is your bid?: $300
Are there any other bidders? Type 'yes' or 'no'.
no
```

**Sample Output:**
```python
The winner is Alice with a bid of $300
```

## How the Program Works
1. The program starts by displaying an ASCII logo and a welcome message.
2. It prompts users to enter their name and bid. This continues until there are no more bidders.
3. After all bids are placed, the program determines the highest bid and prints the winner’s name along with their bid.
4. The screen is cleared after each bid to keep the interface clean.
