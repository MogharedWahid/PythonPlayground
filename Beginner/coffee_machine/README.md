# Coffee Machine Project
A Python-based coffee machine simulator that allows users to select a drink, insert coins, and manage resources such as water, milk, and coffee. The machine supports making three drinks: Espresso, Latte, and Cappuccino. The program checks for sufficient resources, processes the user's payment, and gives change if necessary.

## Features
* Drink Selection: Users can choose from three drinks: Espresso, Latte, and Cappuccino.
* Resource Management: The machine checks if enough water, milk, and coffee are available before making a drink.
* Payment System: Users insert coins (quarters, dimes, nickels, and pennies) to make a payment.
* Change Calculation: The machine returns the correct change if the user provides more money than needed.
* Report Generation: Users can request a report of the current resources and profit.

## Getting Started

To get a copy of this project up and running on your local machine, follow these simple steps:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/MogharedWahid/PythonPlayground.git
   cd PythonPlayground/coffee_machine
  
2. **Run the simulator:**

  ```bash
  python coffee_machine.py
  ```

## Usage
Upon running the program, you will be prompted to choose a drink. The available options are:

* espresso
* latte
* cappuccino
  
You can also input:
* 'report': To see the current status of resources and the total profit.
* 'off': To turn off the coffee machine

## Example Interaction:
```bash
What would you like? (espresso/latte/cappuccino): latte
Please insert coins.
How many quarters?: 2
How many dimes?: 1
How many nickles?: 1
How many pennies?: 2
Here is your latte ☕ Enjoy!
Here is $0.05 in change.
```

## How It Works
1. Choose a Drink: The user selects a drink (Espresso, Latte, or Cappuccino).
2. Check Resources: The program checks if there are enough resources (water, milk, coffee) for the selected drink.
3. Process Payment: The user is prompted to insert coins, and the program calculates the total amount of money inserted.
4. Transaction Check: The program verifies if the user has inserted enough money. If the payment is sufficient, the coffee is made, and the resources are updated.
5. Change: If the user paid more than the required amount, the program calculates and returns the change.
6. Profit Tracking: The total profit from all transactions is tracked and displayed when requested.

## Example Report:
```bash
Water: 300ml
Milk: 200ml
Coffee: 100g
Money: $0.0
```

## Handling Errors
* If the user enters a non-numeric value for coins, the program will prompt the user to enter valid numbers.
* If there are insufficient resources, a specific message will be displayed (e.g., "Sorry there is not enough water").
* If the user doesn't insert enough money, the program will notify them and refund the money.
