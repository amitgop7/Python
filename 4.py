#4. Write a program to check voting eligibility based on:
#● Age ≥ 18
#● Citizenship status

age = int(input("Enter age: "))
citizen = input("Are you a citizen? (yes/no): ").lower()

if age >= 18 and citizen == "yes":
    print("Eligible to vote")
else:
    print("Not eligible to vote")
