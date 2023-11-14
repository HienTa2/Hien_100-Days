# Imports for handling different aspects of the coffee machine operation.
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Initialize the main components of the coffee machine.
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

# Main control flag for the application loop.
is_on = True

# Main application loop.
while is_on:
    # Displaying the current menu options to the user.
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ").lower()

    # Handling the 'off' command to shut down the machine.
    if choice == "off":
        is_on = False
    # Generating and displaying reports from coffee maker and money machine.
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    # Processing the user's drink selection.
    elif choice in options.split('/'):
        # Retrieve the selected drink's details.
        drink = menu.find_drink(choice)

        # Check resource availability and process payment before making coffee.
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
    else:
        # Inform the user about an invalid selection.
        print("Invalid selection. Please choose a valid option.")
