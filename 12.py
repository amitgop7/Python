# 12. Write a program of while loop that keeps asking the user to
# enter a number until they enter 0.

number = int(input("Enter a number: "))

while number != 0:
    print("Not zero")
    number = int(input("Enter a number: "))

print("Zero Entered. ADIOS")
