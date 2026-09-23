#6. Write a program that accepts a single character and checks
#whether it is: (Use if-elif-else)
#● Uppercase letter
#● Lowercase letter
#● Digit
#● Special character

ch = input("Enter a character: ")

if ch.isupper():
    print("Uppercase letter")
elif ch.islower():
    print("Lowercase letter")
elif ch.isdigit():
    print("Digit")
else:
    print("Special character")
