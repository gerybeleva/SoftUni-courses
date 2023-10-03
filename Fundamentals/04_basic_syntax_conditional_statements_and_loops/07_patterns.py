number = int(input())

for i in range (1, number+1):
    for j in range (i):
        print(end='*')
    print()

for n in range (number-1, 0, -1):
    for m in range(n):
        print(end='*')
    print()