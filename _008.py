import math

sqlist = []
for x in range(1, 11):
	sqlist.append(x * x)

print(sqlist) # prints [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

sqlist = [ x * x for x in range(1,11)]
print(sqlist) # prints [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

sqlist = [x * x for x in range(1,11) if x%2 != 0]
print(sqlist) # prints [1, 9, 25, 49, 81]

