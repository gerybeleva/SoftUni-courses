num = int(input())

# Reversed Order
num1 = num
while num1 > 0:
	digit = num1 % 10
	# print(digit)
	num1 = num1 // 10
	print(digit)

# Normal Order
for i in range(len(str(num))):
	string = str(num)
	print(int(string[i]))