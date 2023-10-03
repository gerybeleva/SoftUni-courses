import sys

number = int(input())

total = 0
max_num = -sys.maxsize

for _ in range(number):
    num = int(input())
    total += num
    if num > max_num:
        max_num = num

if total - max_num == max_num:
    print(f'Yes\nSum = {max_num}')
else:
    diff = abs(max_num - (total - max_num))
    print(f'No\nDiff = {diff}')


