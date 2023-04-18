num1 = int(input("enter a number "))
num2 = int(input("enter a number "))
divider = 2
array = []
while num1 > 1:
    if num1 % divider == 0:
        num1 = num1 / divider
        array.append(divider)
    else:
        divider += 1
divider2 = 2
(array2) = []
while num2 > 1:
    if num2 % divider2 == 0:
        num2 = num2 / divider2
        array2.append(divider2)
    else:
        divider2 += 1


newArray = []

for i in array:
    for j in array2:
        if i == j and j not in newArray:
            newArray.append(j)
print(newArray)
