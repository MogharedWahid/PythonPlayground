logo = """
 ██████╗ ██████╗ ███████╗███████╗███████╗███████╗    ███╗   ███╗ █████╗  ██████╗██╗  ██╗██╗███╗   ██╗███████╗
██╔════╝██╔═══██╗██╔════╝██╔════╝██╔════╝██╔════╝    ████╗ ████║██╔══██╗██╔════╝██║  ██║██║████╗  ██║██╔════╝
██║     ██║   ██║█████╗  █████╗  █████╗  █████╗      ██╔████╔██║███████║██║     ███████║██║██╔██╗ ██║█████╗  
██║     ██║   ██║██╔══╝  ██╔══╝  ██╔══╝  ██╔══╝      ██║╚██╔╝██║██╔══██║██║     ██╔══██║██║██║╚██╗██║██╔══╝  
╚██████╗╚██████╔╝██║     ██║     ███████╗███████╗    ██║ ╚═╝ ██║██║  ██║╚██████╗██║  ██║██║██║ ╚████║███████╗
 ╚═════╝ ╚═════╝ ╚═╝     ╚═╝     ╚══════╝╚══════╝    ╚═╝     ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝╚══════╝
                                                                                                             
"""
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0

def choose_drink():
    drink_f = input("What would you like? (espresso/latte/cappuccino): ").lower()
    return drink_f

def print_report():
    global resources
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit}")


def check_resources(drink_f):
    # Check water, coffee, and milk (if applicable)
    if resources['water'] < MENU[drink_f]['ingredients']['water']:
        print("Sorry there is not enough water.")
        return False
    if resources['coffee'] < MENU[drink_f]['ingredients']['coffee']:
        print("Sorry there is not enough coffee.")
        return False
    if drink_f != 'espresso' and resources['milk'] < MENU[drink_f]['ingredients']['milk']:
        print("Sorry there is not enough milk.")
        return False

    return True

def process_coins():
    print("Please insert coins.")
    try:
        quarters = float(input("How many quarters?: "))
        dimes = float(input("How many dimes?: "))
        nickles = float(input("How many nickles?: "))
        pennies = float(input("How many pennies?: "))
    except ValueError:
        print("Invalid input, please enter numeric values.")
        return 0
    paid_money_f = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * .01
    return paid_money_f

def check_transaction(paid_money_f, drink_f):
    return paid_money_f >= MENU[drink_f]['cost']

def make_coffee(drink_f, paid_money_f):
    global profit
    resources['water'] -= MENU[drink_f]['ingredients']['water']
    resources['coffee'] -= MENU[drink_f]['ingredients']['coffee']
    if drink_f != 'espresso':
        resources['milk'] -= MENU[drink_f]['ingredients']['milk']
    print(f"Here is your {drink_f} ☕ Enjoy!")
    profit += MENU[drink_f]['cost']
    if paid_money_f > MENU[drink_f]['cost']:
        change = paid_money_f - MENU[drink_f]['cost']
        print(f"Here is ${change:.2f} in change.")


drink= ''
print(logo)
while drink != 'off':
    drink = choose_drink()
    if drink == 'off':
        break
    elif drink == 'report':
        print_report()
    elif drink == 'espresso' or drink == 'latte' or drink == 'cappuccino':
        if check_resources(drink):
            paid_money = process_coins()
            if check_transaction(paid_money, drink):
                make_coffee(drink, paid_money)
            else:
                print("Sorry that's not enough money. Money refunded.")
                continue
    else:
        print("Invalid input!")
        continue


