#16. Write a program to print a multiplication table of a number(user input).

num = int(input("Enter number: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)
