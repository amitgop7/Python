#17. Write a program to print numbers divisible by 4 in a range.

start = int(input("Enter start: "))
end = int(input("Enter end: "))

for i in range(start, end+1):
    if i % 4 == 0:
        print(i)
