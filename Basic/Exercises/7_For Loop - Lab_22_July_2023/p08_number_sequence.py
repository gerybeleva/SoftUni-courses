import sys
from sys import maxsize

number =  int(input())
max_number = -maxsize
min_number = maxsize

for _ in range(number):
    num = int(input())
    if num > max_number:
        max_number = num

    if num < min_number:
        min_number = num

print(f'Max number: {max_number}')
print(f'Min number: {min_number}')