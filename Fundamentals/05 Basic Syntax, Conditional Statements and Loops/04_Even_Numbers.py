n = int(input())
even = False

for i in range(n):
	num = int(input())
	if not num % 2 == 0:
		print(f'{num} is odd!')
		break
else:
	print(f'All numbers are even.')