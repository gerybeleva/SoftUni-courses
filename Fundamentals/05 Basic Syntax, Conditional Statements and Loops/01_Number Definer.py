number = float(input())
definer = ''

if number == 0:
	print('zero')
if number > 0:
	definer = 'positive'
	if 0 < abs(number) < 1: print(f'small {definer}')
	elif 1 <= abs(number) <= 1000000: print(f'{definer}')
	else: print(f'large {definer}')

if number < 0:
	definer = 'negative'
	if 0 < abs(number) < 1: print(f'small {definer}')
	elif 1 <= abs(number) <= 1000000: print(f'{definer}')
	else: print(f'large {definer}')