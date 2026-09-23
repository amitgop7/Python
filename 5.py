#5. Write a program to check whether a number is divisible by 2
#and 3 both.

num = int(input("Enter number: "))

if num % 2 == 0 and num % 3 == 0:
    print("Divisible by both 2 and 3")
else:
    print("Not divisible by both 2 and 3")
