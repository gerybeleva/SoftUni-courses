num1 = int(input())
num2 = num1

total_left = 0
total_right = 0

for _ in range(num1):
    left_num = int(input())
    total_left += left_num

for _ in range(num2):
    right_num = int(input())
    total_right += right_num

if total_left ==  total_right:
    print(f'Yes, sum = {total_left}')
else:
    diff = abs(total_left - total_right)
    print(f'No, diff = {diff}')