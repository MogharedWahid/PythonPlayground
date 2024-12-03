from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

logo = """
 ██████╗ ██████╗ ███████╗███████╗███████╗███████╗    ███╗   ███╗ █████╗  ██████╗██╗  ██╗██╗███╗   ██╗███████╗
██╔════╝██╔═══██╗██╔════╝██╔════╝██╔════╝██╔════╝    ████╗ ████║██╔══██╗██╔════╝██║  ██║██║████╗  ██║██╔════╝
██║     ██║   ██║█████╗  █████╗  █████╗  █████╗      ██╔████╔██║███████║██║     ███████║██║██╔██╗ ██║█████╗  
██║     ██║   ██║██╔══╝  ██╔══╝  ██╔══╝  ██╔══╝      ██║╚██╔╝██║██╔══██║██║     ██╔══██║██║██║╚██╗██║██╔══╝  
╚██████╗╚██████╔╝██║     ██║     ███████╗███████╗    ██║ ╚═╝ ██║██║  ██║╚██████╗██║  ██║██║██║ ╚████║███████╗
 ╚═════╝ ╚═════╝ ╚═╝     ╚═╝     ╚══════╝╚══════╝    ╚═╝     ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝╚══════╝

"""

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

drink= ''
print(logo)
while drink != 'off':
    drink = input(f"What would you like? ({menu.get_items()}): ").lower()
    if drink == 'off':
        break
    elif drink == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        menu_item = menu.find_drink(drink)
        if menu_item:
            if coffee_maker.is_resource_sufficient(menu_item):
                if money_machine.make_payment(menu_item.cost):
                    coffee_maker.make_coffee(menu_item)
                else:
                    continue
            else:
                continue
        else:
            continue
