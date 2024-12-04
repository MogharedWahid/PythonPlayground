# Coffee Machine Project

This is a Python-based coffee machine simulation project designed to practice Object-Oriented Programming (OOP) principles. The program models a coffee machine that can serve different drinks, manage available resources (water, milk, coffee), and process payments. It simulates the process of making coffee by checking for sufficient resources, receiving payment, and providing change if necessary.

## Project Overview

The project consists of three main classes:

1. **CoffeeMaker**: Manages the available resources (water, milk, coffee) and checks if the machine can make a particular drink based on the available resources.
2. **Menu**: Contains the list of available coffee drinks, including the ingredients and cost for each item.
3. **MoneyMachine**: Handles the payment process, including accepting coins and ensuring the user inserts enough money for the selected drink.

The `main.py` file ties everything together by running an interactive loop where users can choose a drink, check resources, and make payments.

## Features

- **Interactive User Interface**: Users can input their orders and check available resources.
- **Resource Management**: Tracks the available water, milk, and coffee, and deducts the resources when a drink is made.
- **Payment System**: Allows users to insert coins, calculates the total, and ensures that the payment is sufficient before making the coffee.
- **Drink Menu**: Offers a selection of drinks, including latte, espresso, and cappuccino, each with its own ingredients and cost.
- **Reports**: Users can request a report of the current resources and the money collected by the machine.

## Getting Started

To get a copy of this project up and running on your local machine, follow these simple steps:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/MogharedWahid/PythonPlayground.git
   cd PythonPlayground/intermediate/coffee_machine
  
2. **Run the simulator:**

  ```bash
  python main.py
  ```

## Usage
Once the program is running, you'll be prompted to choose a drink from the available options (latte, espresso, cappuccino). You can also type report to check the current resources or off to stop the machine.

## Example:
```plaintext
What would you like? (latte/espresso/cappuccino/): latte
Please insert coins.
How many quarters?: 2
How many dimes?: 1
How many nickles?: 0
How many pennies?: 3
Here is $0.73 in change.
Here is your latte ☕️. Enjoy!
```

## Commands:
* **off**: Turns off the coffee machine.
* **report**: Displays a report of available resources and the current profit.

### How It Works
The program consists of several components working together:

1. **Menu**: Stores the drinks and their ingredients.
2. **CoffeeMaker**: Deducts resources when a drink is made and checks if there are enough resources to prepare the selected drink.
3. **MoneyMachine**: Handles the user's coin inputs, checks if the payment is sufficient, and processes the transaction.

## Example Code Flow:
* The user selects a drink from the menu.
* The program checks if the machine has enough resources to make the drink.
* The user is prompted to insert coins. If the payment is sufficient, the drink is made, and the appropriate resources are deducted.
* If there's change, it is returned to the user.
* The program continues running until the user types off.

