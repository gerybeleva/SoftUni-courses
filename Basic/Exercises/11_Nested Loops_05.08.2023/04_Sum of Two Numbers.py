in_number = int(input())
out_number = int(input())
magic_number = int(input())
combination = 0
i = 0
j = 0
flag = False

for i in range(in_number, out_number + 1):
    for j in range(in_number, out_number + 1):
        combination += 1
        if i + j == magic_number:
            flag = True
            break
    if flag:
        break
if i + j == magic_number:
    print(f'Combination N:{combination} ({i} + {j} = {magic_number})')
else:
    print(f'{combination} combinations - neither equals {magic_number}')