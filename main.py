import art
print(art.logo)

def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    if n2 == 0:
        raise ValueError("Cannot divide by zero")
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def get_input():
    while True:
        try:
            return float(input("What is the first number? "))
        except ValueError:
            print("Please enter a valid number.")

number1 = get_input()



keep_going = True
while keep_going:




    operator = input("""
    +
    -
    *
    /
Pick an operation: """)

    if operator not in operations:
        print("Invalid operator")
        continue

    number2 = get_number("What is the next number? ")

    try:
        result = str(operations[operator](number1, number2))
        print(f"The answer is: {result}")
    except ValueError as e:
        print(e)
        continue

    choice = input(f"Type '1' to keep calculating with {result}, '2' to start a new calculation, '3' to exit. ")
    if choice == "1":
        number1 = float(result)
    elif choice == "2":
        number1 = get_number("What is the first number? ")
    elif choice == "3":
        exit()
    else:
        print("Invalid choice. Starting new calculation.")
        number1 = get_number("What is the first number? ")



