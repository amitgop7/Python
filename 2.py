#2. Write a program that accepts marks in five subjects. (Use if -else)
#● If any subject has marks less than 40 → Fail
#● Else calculate average and display:
#○ ≥ 75 → Distinction
#○ ≥ 60 → First Division
#○ ≥ 50 → Second Division
#○ Else → Pass

marks = []
for i in range(5):
    marks.append(int(input(f"Enter marks of subject {i+1}: ")))

if any(m < 40 for m in marks):
    print("Fail")
else:
    avg = sum(marks) / 5
    if avg >= 75:
        print("Distinction")
    elif avg >= 60:
        print("First Division")
    elif avg >= 50:
        print("Second Division")
    else:
        print("Pass")
