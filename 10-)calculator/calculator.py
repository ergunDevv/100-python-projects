import art
print(art.logo)


def add(n1, n2):
    return n1+n2


def subtract(n1, n2):
    return n1-n2


def multiply(n1, n2):
    return n1*n2


def divide(n1, n2):
    return n1/n2


operations = {"+": add, "-": subtract, "*": multiply, "/": divide, }


def calculation():
    num1 = float(input("What's the first number?: "))
    num2 = float(input("What's the second number?: "))

    for func in operations:
        print(func)
    operation_symbol = input("Pick an operation from line above: ")

    first_answer = operations[operation_symbol](num1, num2)

    print(f"{num1} {operation_symbol} {num2} = {first_answer}")

    if input(f"Type 'y' to continue calculating with {first_answer}, or type 'n' to start a new calculation.: ") == 'y':
        continue_var = True
    else:
        print(art.logo)

        calculation()

    while continue_var:
        num3 = int(input("What's the next number?: "))

        for func in operations:
            print(func)
        operation_symbol = input("Pick an operation from line above: ")
        answer = operations[operation_symbol](first_answer, num3)
        print(f"{first_answer} {operation_symbol} {num3} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit.: ") == 'y':
            continue_var = True
        else:
            calculation()


calculation()
