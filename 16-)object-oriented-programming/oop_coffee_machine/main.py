from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()
menu_items = menu.get_items()

while True:
    coffee_type = input(f"What would you like? ({menu.get_items()}): ")
    coffee = menu.find_drink(coffee_type)
    if coffee_type == 'off':
        break
    if coffee_type == 'report':
        coffee_machine.report()
        # dont need for loop

    if coffee_machine.is_resource_sufficient(coffee):
        if money_machine.make_payment(coffee.cost):
            coffee_machine.make_coffee(coffee)
