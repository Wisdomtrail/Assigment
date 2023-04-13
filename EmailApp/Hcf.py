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
length = array.__len__()
length2 = array2.__len__()
print(length, length2)
minCounter = min(length, length2)
