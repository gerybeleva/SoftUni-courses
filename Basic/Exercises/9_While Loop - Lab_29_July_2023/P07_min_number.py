from sys import maxsize

min = maxsize

console_input = input()

while console_input != 'Stop':
    number = int(console_input)

    if number < min:
        min = number
    console_input = input()

print(min)