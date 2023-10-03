budget = int(input())
console = input()

while console != 'End':
	price = int(console)
	budget -= price
	if budget < 0:
		print('You went in overdraft!')
		break
	console = input()
else:
	print('You bought everything needed.')
