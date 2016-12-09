import math

# two versions of programme

anumber = int(input("Please enter an integer"))
print(math.sqrt(abs(anumber)))
# with int 44 = 6.63324958071


anumber1 = int(input("Please enter an integer"))
if anumber1 < 0:
	print("not a positive integer. I will use the absolute value")
	print(math.sqrt(abs(anumber1)))
else:
	print(math.sqrt((anumber1number)))
	
# with -55, prints
# not a positive integer. I will use the absolute value
# 7.4161984871

