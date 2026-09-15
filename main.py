#We implemented a simple coffee maker
#Select your option (espresso, latte, cappuccino) for coffee
#Type 'off' to turn off the machine
#Type 'report' to see what remaining resources the machine has

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

def main():
    make_coffee = CoffeeMaker()
    payment = MoneyMachine()
    coffee_menu = Menu()
    choice = ""

    while choice != "off":
        choice = input("What would you like? (espresso/latte/cappuccino/):")
        if choice not in ['espresso', 'latte', 'cappuccino', 'off', 'report']:
            print("Invalid option.\n")
            choice = input("What would you like? (espresso/latte/cappuccino/):")
        if choice == "report":
            make_coffee.report()
            payment.report()
            continue
        if choice == "off":
            break
        menu_item = coffee_menu.find_drink(choice)
        if make_coffee.is_resource_sufficient(menu_item):
            if payment.make_payment(menu_item.cost):
                make_coffee.make_coffee(menu_item)

main()
