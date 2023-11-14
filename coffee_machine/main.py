# Menu dictionary with drink types, their ingredients, and costs.
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

# Initial resources in the coffee machine.
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# Starting profit is zero as no drinks have been sold yet.
profit = 0


def is_resource_sufficient(order_ingredients):
    """Checks if resources are sufficient for the ordered drink.
    Args:
        order_ingredients (dict): A dictionary of ingredients needed for the drink.
    Returns:
        bool: True if resources are enough, False otherwise.
    """
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    """Processes coin input from the user and calculates the total money inserted.
    Returns:
        float: The total amount of money inserted.
    """
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """Checks if the user has inserted enough money to purchase the drink.
    Args:
        money_received (float): The total amount of money inserted.
        drink_cost (float): The cost of the drink.
    Returns:
        bool: True if the transaction is successful, False otherwise.
    """
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        global profit
        profit += drink_cost
        if change > 0:
            print(f"Here is ${change} in change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(choice, order_ingredients):
    """Deducts the required ingredients from the resources.
    Args:
        choice (str): The user's chosen drink.
        order_ingredients (dict): The ingredients required for the drink.
    """
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {choice} ☕️. Enjoy!")


# Main program
is_on = True
while is_on:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_choice == "off":
        is_on = False
    elif user_choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU.get(user_choice)
        if drink and is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(user_choice, drink["ingredients"])

# If the while loop is exited, the machine turns off.
print("Turning off the coffee machine.")
