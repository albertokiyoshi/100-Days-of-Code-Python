MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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
    "money": 0,
}


# Reporting resources
def report_resources():
    print(f"""Water: {resources["water"]}ml 
Milk: {resources["milk"]}ml
Coffee: {resources["coffee"]}ml
Money: ${resources["money"]}
    """)


# Checking if there are sufficient resources
def check_resources(drink_ingredients):
    for item in drink_ingredients:
        if drink_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


# Processing coins
def process_coins():
    coins = {}
    print("Please insert coins.")
    coins["quarters"] = int(input("How many quarters? "))
    coins["dimes"] = int(input("How many dimes? "))
    coins["nickles"] = int(input("How many nickles? "))
    coins["pennies"] = int(input("How many pennies? "))
    return coins["quarters"] * 0.25 + coins["dimes"] * 0.1 + coins["nickles"] * 0.05 + coins["pennies"] * 0.01


# Checking if costumer inserted enough money
def check_money(drink):
    coins_value = process_coins()
    if coins_value == MENU[drink]["cost"]:
        print(f"Here is your {drink} ☕️. Enjoy!")
        resources["water"] -= MENU[drink]["ingredients"]["water"]
        resources["milk"] -= MENU[drink]["ingredients"]["milk"]
        resources["coffee"] -= MENU[drink]["ingredients"]["coffee"]
        resources["money"] += MENU[drink]["cost"]
    elif coins_value > MENU[drink]["cost"]:
        change = round(coins_value - MENU[drink]["cost"], 2)
        print(f"Here is ${change} in change.")
        print(f"Here is your {drink} ☕️. Enjoy!")
        resources["water"] -= MENU[drink]["ingredients"]["water"]
        resources["milk"] -= MENU[drink]["ingredients"]["milk"]
        resources["coffee"] -= MENU[drink]["ingredients"]["coffee"]
        resources["money"] += MENU[drink]["cost"]
    else:
        print("Sorry that's not enough money. Money refunded.")


turn_off = False
while not turn_off:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice in MENU:
        if check_resources(MENU[choice]["ingredients"]):
            check_money(choice)
    elif choice == "report":
        report_resources()
    elif choice == "off":
        turn_off = True