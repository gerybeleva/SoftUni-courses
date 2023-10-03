n = int(input())

num = 0
flag = False
for row in range(1, n + 1):
    for column in range(1, row + 1):
        num += 1
        print(num, end=' ')
        if num == n:
            flag = True
            break
    print()
    if flag:
        break
