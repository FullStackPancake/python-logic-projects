import art

print(art.logo)

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b

def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

operation = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

for i in operation:
    print(i)

print("Welcome to the calculator")
a = float(input("Enter the first number: "))
while True:

    calculator = input("Enter the calculator: ( * / + - ) : ")
    b = float(input("Enter the second number: "))

    # if calculator == "+":
    #     result = add(a,b)
    # elif calculator == "-":
    #     result = subtract(a,b)
    # elif calculator == "*":
    #     result = multiply(a,b)
    # elif calculator == "/":
    #     if b == 0:
    #         print("Can not divide by zero")
    #         continue
    #     result = divide(a,b)
    # else:
    #     print("Please enter a valid operation")
    #     continue
    #
    # print(f"The result is: ")

    if calculator in operation:
        if calculator == "/" and b == 0:
            print("Cannot divide by zero")
            continue

        new_cal = operation[calculator]
        result = new_cal(a,b)
        print(result)

    else:
        print("Invalid operation")
        continue

    while True:
        next_number = input(f"continue calculating with same number {result} (y) \n "
                            "start a new calculation (n) \n "
                            "leave the calculator (l) \n").lower()
        if next_number == "y":
            a = result
            break

        elif next_number == "n":
            a = float(input("Enter the first number: "))
            break

        elif next_number == "l":
            print("Thank you for using this calculator")
            exit()

        else:
            print("Invalid selection, please choose 'y', 'n' or 'l'")