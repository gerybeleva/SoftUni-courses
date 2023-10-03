num = int(input())

total_even = 0
total_odd = 0

for i in range(num):
    current_num = int(input())

    if i % 2 == 0:
        total_even += current_num
    else:
        total_odd += current_num

if total_even == total_odd:
    print(f'Yes\nSum = {total_even}')
else:
    diff = abs(total_even - total_odd)
    print(f'No\nDiff = {diff}')