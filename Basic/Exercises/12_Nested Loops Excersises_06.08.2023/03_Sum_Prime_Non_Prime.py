console_input = input()


sum_prime_numbers = 0
sum_regular_numbers = 0

while console_input != 'stop':
    digit = int(console_input)
    if digit < 0:
        print('Number is negative.')
        console_input = input()
        continue

    simple_digit_counter = 0
    for i in range(1, digit + 1):
        if digit % i == 0:
            simple_digit_counter += 1

    if simple_digit_counter == 2:
        sum_prime_numbers += digit
    else:
        sum_regular_numbers += digit

    console_input = input()

print(f'Sum of all prime numbers is: {sum_prime_numbers}')
print(f'Sum of all non prime numbers is: {sum_regular_numbers}')