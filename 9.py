#9. Create a calculator using match-case that:
#● Accepts two numbers
#● Allows the user to choose an operation (+, -, *, /, %)#
#● Displays appropriate error message for invalid choice or division by zero

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operation (+,-,*,/,%) : ")

match op:
    case "+":
        print(a + b)
    case "-":
        print(a - b)
    case "*":
        print(a * b)
    case "/":
        if b != 0:
            print(a / b)
        else:
            print("Division by zero error")
    case "%":
        if b != 0:
            print(a % b)
        else:
            print("Division by zero error")
    case _:
        print("Invalid operation")
