#8. Write a program to check the insurance eligibility. (Use nested if) Accept age and annual income from the user.
#● Age ≥ 18 and income ≥ 3,00,000 → Eligible
#● Age ≥ 18 and income < 3,00,000 → Not Eligible (Low Income)
# ● Age < 18 → Not Eligible (Underage)

age = int(input("Enter age: "))
income = int(input("Enter annual income: "))

if age >= 18:
    if income >= 300000:
        print("Eligible")
    else:
        print("Not Eligible (Low Income)")
else:
    print("Not Eligible (Underage)")
