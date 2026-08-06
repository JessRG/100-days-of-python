from art import logo

def add(n1, n2):
    return n1 + n2

# TODO: Write out the other 3 functions - subtract, multiply and divide.
def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

# TODO: Add these 4 functions into a dictionary as the values. Keys = "+", "-", "*", "/"
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

# TODO: Use the dictionary operations to perform the calculations. Multiply 4 * 8 using the dictionary.
# print(operations["*"](4, 8))

result = 0
continue_with_result = False
while True:
    print(logo)

    if not continue_with_result:
        num1 = float(input("What is the first number?: "))
    else:
        num1 = result

    for operation in operations:
        print(operation)
    op = input("Pick an operation: ")
    num2 = float(input("What is the next number?: "))

    if op in operations:
        result = operations[op](num1, num2)

    print(f"{num1} {op} {num2} = {result}")

    calc_with_result = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()

    if calc_with_result in ("y", "yes"):
        continue_with_result = True
    else:
        continue_with_result = False
        print("\n" * 20)
