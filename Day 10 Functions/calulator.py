from art import logo

print(logo)


def add(n1, n2):
    """
    Returns the sum of two numbers.

    Parameters:
    - n1, n2: The numbers to be added.

    Returns:
    - float: The sum of n1 and n2.
    """
    return n1 + n2


def subtract(n1, n2):
    """
    Returns the difference between two numbers.

    Parameters:
    - n1, n2: The numbers to be subtracted (n1 - n2).

    Returns:
    - float: The difference between n1 and n2.
    """
    return n1 - n2


def multiply(n1, n2):
    """
    Returns the product of two numbers.

    Parameters:
    - n1, n2: The numbers to be multiplied.

    Returns:
    - float: The product of n1 and n2.
    """
    return n1 * n2


def divide(n1, n2):
    """
    Returns the quotient of two numbers.

    Parameters:
    - n1, n2: The numbers to be divided (n1 / n2).

    Returns:
    - float: The quotient of n1 and n2.
    - str: A message if division by zero is attempted.
    """
    if n2 == 0:
        return "Cannot divide by zero!"
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    """
    Performs calculations based on user input and displays the result.
    Continues to perform calculations with the previous result until the user decides to start a new calculation.
    """
    num1 = float(input("What is the first number?: "))

    for key in operations:
        print(key)

    should_continue = True
    while should_continue:
        operations_symbol = input("Pick an operation from the list above: ")
        num2 = float(input("What is the next number?: "))

        if operations_symbol not in operations:
            print("Invalid operation. Try again.")
            continue

        calculation_function = operations[operations_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operations_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
            num1 = answer
        else:
            should_continue = False


# Main execution
while True:
    calculator()
    if input("Type 'n' to exit, or any other key to start a new calculation: ") == 'n':
        break
