#18. Write a program to print factorial of a number using for loop.

num = int(input("Enter number: "))
fact = 1

for i in range(1, num+1):
    fact *= i

print("Factorial:", fact)
