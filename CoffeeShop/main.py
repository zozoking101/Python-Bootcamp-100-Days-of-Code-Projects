def is_res_suff(ing):
    """Returns True when order can be made, False otherwise"""
    for _ in ing:
        if ing[_] >= resources[_]:
            print(f"Sorry there is not enough {_}.")
            return False
        return True


def process_coins():
    """Returns the total calculated from coins inserted"""
    print("Please insert coins.")
    total = 0
    total += int(input("How many quarters: ")) * 0.25
    total += int(input("How many dimes: ")) * 0.10
    total += int(input("How many nickels: ")) * 0.05
    total += int(input("How many pennies: ")) * 0.01
    return total


def is_trans_succ(received, cost):
    """Returns True if payment accepted, False otherwise"""
    if received >= cost:
        change = round(received - cost, 2)
        if change > 0:
            print(f"Here is ${change} in change.")
        global profit
        profit += cost
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, ing):
    """Deduct the required ingredients from resources"""
    for item in ing:
        resources[item] -= ing[item]
    print(f"Here is your {drink_name} ☕")


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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

machine_running = True


while machine_running:
    query = input("What would you like? (espresso/latte/cappuccino): ")

    if query.lower() == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}ml")
        print(f"Money: ${profit}")

    elif query.lower() == 'off':
        machine_running = False

    else:
        drink = MENU[query]
        if is_res_suff(drink['ingredients']):
            payment = process_coins()
            if is_trans_succ(payment, drink["cost"]):
                make_coffee(query, drink["ingredients"])
