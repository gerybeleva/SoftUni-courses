
balance = 0

while True:
    console_input = input()

    if console_input == 'NoMoreMoney':
        break

    current_sum = float(console_input)

    if current_sum >= 0:
        balance += current_sum
        print(f'Increase: {current_sum:.02f}')

    else:
        print('Invalid operation!')
        break

print(f'Total: {balance:.02f}')