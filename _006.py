counter = 1
while counter <= 5:
	print("Hello world")
	counter = counter + 1
	
# prints "Hello world" five times

for item in [1, 3, 6, 2, 5]:
	print(item)

# prints 1 3 6 2 5

for item in range(5):
	print(item ** 2)
	
# prints 0 1 4 9 16

for aword in wordlist:
	for aletter in aword:
		letterlist.append(aletter)
	print(letterlist)
	
# ['c', 'a', 't']
# ['c', 'a', 't', 'd', 'o', 'g']
# ['c', 'a', 't', 'd', 'o', 'g', 'r', 'a', 'b', 'b', 'i', 't']

n = 10
if n < 0:
	print("Sorry, value is negative")
else:
	print(math.sqrt(n))
	
# prints 3.16227766017

