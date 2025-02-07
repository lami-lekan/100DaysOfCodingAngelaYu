def add(n1, n2):
    """Adds two numbers"""
    return n1 + n2


def subtract(n1, n2):
    """Subtract two numbers"""
    return n1 - n2


def divide(n1, n2):
    """Divides two numbers"""
    return n1 / n2


def multiply(n1, n2):
    """Multiply two numbers"""
    return n1 * n2

def calc_continue(number):
    operation_dict = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide,
    }
    operation = input("+\n-\n*\n/\nPick an operation: ")
    next_number = float(input("What's the next number?: "))
    return operation_dict[operation](number, next_number)

def calculator():
    operation_dict = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide,
    }
    first_number = float(input("What's the first number?: "))
    operation = input("+\n-\n*\n/\nPick an operation: ")
    next_number = float(input("What's the next number?: "))
    # if operation == '+':
    #     result = add(first_number, next_number)
    #     print(f"{first_number} {operation} {next_number} = {result}")
    # elif operation == '-':
    #     result = subtract(first_number, next_number)
    #     print(f"{first_number} {operation} {next_number} = {result}")
    # elif operation == '*':
    #     result = multiply(first_number, next_number)
    #     print(f"{first_number} {operation} {next_number} = {result}")
    # elif operation == '/':
    #     result = divide(first_number, next_number)
    #     print(f"{first_number} {operation} {next_number} = {result}")
    # else:
    #     print("Invalid operation!")

    result = operation_dict[operation](first_number, next_number)
    print(f"{first_number} {operation} {next_number} = {result}")
    choice = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
    while choice == 'y':
        print(calc_continue(result))
        choice = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
    calculator()



calculator()
