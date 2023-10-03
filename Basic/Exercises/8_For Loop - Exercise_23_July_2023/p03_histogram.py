import random

number = int(input())
p1 = 0  # <200
p2 = 0  # 200 < 399
p3 = 0  # 400 < 599
p4 = 0  # 600 < 799
p5 = 0  # > 800

for _ in range(number):
    n = int(input())
    if n < 200:
        p1 += 1
    elif 200 <= n < 400:
        p2 += 1
    elif 400 <= n < 600:
        p3 += 1
    elif 600 <= n < 800:
        p4 += 1
    else:
        p5 += 1

h1 = p1 / number * 100
h2 = p2 / number * 100
h3 = p3 / number * 100
h4 = p4 / number * 100
h5 = p5 / number * 100

print(f'{h1:.02f}%')
print(f'{h2:.02f}%')
print(f'{h3:.02f}%')
print(f'{h4:.02f}%')
print(f'{h5:.02f}%')
