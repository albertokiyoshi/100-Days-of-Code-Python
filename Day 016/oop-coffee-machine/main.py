from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

drink_items = Menu()
coffee_machine = CoffeeMaker()
charging = MoneyMachine()

turn_off = False

while not turn_off:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        turn_off = True
    elif choice == "report":
        coffee_machine.report()
        charging.report()
    else:
        drink = drink_items.find_drink(choice)
        if coffee_machine.is_resource_sufficient(drink) and charging.make_payment(drink.cost):
            coffee_machine.make_coffee(drink)
