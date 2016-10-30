import math
print([1,3, True, 6.5])
myList = [1, 3, True, 6.5]
print(myList)
potato = myList * 6
print(potato) #prints list six times in one array
myList = [1, 2, 3, 4]
A = [myList] * 3
print(A)
myList[2] = 45
print(A) # prints [1, 2, 45, 5]