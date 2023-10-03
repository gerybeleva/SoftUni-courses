from sys import maxsize

max = -maxsize

console_input = input()

while console_input != 'Stop':
    number = int(console_input)

    if number > max:
        max = number
    console_input = input()

print(max)