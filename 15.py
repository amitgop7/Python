#15. Write a program to print the sum of all digits of user input numbers.

num = input("Enter number: ")
total = 0

for d in num:
    total += int(d)

print("Sum of digits:", total)
