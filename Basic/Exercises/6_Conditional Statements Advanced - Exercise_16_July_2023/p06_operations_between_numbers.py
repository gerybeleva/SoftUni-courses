n1 = int(input())
n2 = int(input())
operator = input()  # "+", "-", "*", "/", "%".
result = 0
digit_type = ''

if operator == '+':
    result = n1 + n2
    if result % 2 == 0:
        digit_type = 'even'
    else:
        digit_type = 'odd'
elif operator == '-':
    result = n1 - n2
    if result % 2 == 0:
        digit_type = 'even'
    else:
        digit_type = 'odd'
elif operator == '*':
    result = n1 * n2
    if result % 2 == 0:
        digit_type = 'even'
    else:
        digit_type = 'odd'
elif operator == '/' and n2 == 0:
    print(f'Cannot divide {n1} by zero')
elif operator == '/' and n2 != 0:
    result = n1 / n2
elif operator == '%' and n2 == 0:
    print(f'Cannot divide {n1} by zero')
elif operator == '%' and n2 != 0:
    result = n1 % n2

if operator == '+' or operator == '-' or operator == '*':
    print(f'{n1} {operator} {n2} = {result} - {digit_type}')
elif operator == '/' and n2 != 0:
    print(f'{n1} {operator} {n2} = {result:.02f}')
elif operator == '%' and n2 != 0:
    print(f'{n1} {operator} {n2} = {result}')
