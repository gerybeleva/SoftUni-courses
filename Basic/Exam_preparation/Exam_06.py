n = int(input())
flag = False
for a in range(1, 10):
    for b in range(9, a, -1):
        for c in range(0, 10):
            for d in range(9, c, -1):
                if (a + b + c + d) == (a * b * c * d) and n % 10 == 5:
                    print(f'{a}{b}{c}{d}')
                    flag = True
                elif 3<= ((a * b * c * d) / (a + b + c + d)) < 4 and n % 3 == 0:
                    print(f'{d}{c}{b}{a}')
                    flag = True
                if flag:
                    break
            if flag:
                break
        if flag:
            break
    if flag:
        break
else:
    print('Nothing found')