#13. Write a program to count even numbers and odd numbers
#stored in a list.

number=[10,12,13,69,99]
oddCount=evenCount=0

for n in number:
    if n%2==0:
        oddCount+=1
    else:
        evenCount+=1

print("Odd numbers: ",oddCount)
print("Even numbers: ",evenCount)
