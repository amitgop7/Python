#14. Write a program to print the following patterns :

#N
#NE
#NEP
#NEPA
#NEPAL

word = "NEPAL"

for i in range(1, 6):
    print(word[:i])

#*
#**
#***
#****

pattern="****"
for i in range(1,5):
    print(pattern[:i])


#    *
#   * *
#  * * *
# * * * *
#* * * * *

pattern = "*****"
rows = len(pattern)

for i in range(1, rows + 1):
    spaces = " " * (rows - i)          
    stars = " ".join(pattern[:i])      
    print(spaces + stars)

#1
#2 3
#4 5 6
#7 8 9 10
    
num = 1
rows = 4

for i in range(1, rows + 1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()

