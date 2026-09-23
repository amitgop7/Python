#7. Write a program using match-case to simulate traffic signals:
#● Red → Stop
#● Yellow → Get Ready
#● Green → Go
#If input is invalid, display an error message.invalid, display an error message.

signal = input("Enter signal color: ").lower()

match signal:
    case "red":
        print("Stop")
    case "yellow":
        print("Get Ready")
    case "green":
        print("Go")
    case _:
        print("Invalid signal")
