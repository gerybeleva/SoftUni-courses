# This a tess for Branch merging. Gery should test it as well.
# calculator app

def calc():
	num1 = float(input('Enter 1st digit: '))
	operator = str(input('Operator: '))
	num2 = float(input('Enter 2nd digit: '))
	result = 0

	if operator == '+':
		result = num1 + num2
		print(f'{num1} + {num2} = {result:.03f}')
	elif operator == '-':
		result = num1 - num2
		print(f'{num1} - {num2} = {result:.03f}')
	elif operator == '*':
		result = num1 * num2
		print(f'{num1} * {num2} = {result:.03f}')
	elif operator == '/' and num2 != 0:
		result = num1 / num2
		print(f'{num1} / {num2} = {result:.03f}')
	else:
		print('Invalid operator!')

action: str = (input('Press Enter to start calculator:'))
print()
while action != 'n' or 'N':
	calc()
	print()
	action = input('---Restart---: Y/N ')
	print()
else:
	print('exit')
