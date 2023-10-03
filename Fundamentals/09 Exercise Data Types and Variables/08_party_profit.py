group_size = int(input())
days_of_adventure = int(input())

every_day = 0

for days in range(1, days_of_adventure+1):
    if days % 10 == 0:
        group_size -= 2
    if days % 15 == 0:
        group_size += 5
    if days % 3 == 0:
        every_day -= group_size * 3
    if days % 5 == 0:
        every_day += group_size * 20
        if days % 3 == 0:
            every_day -= group_size * 2
    every_day += 50
    every_day -= group_size * 2

coins_each_companion = every_day // group_size
print(f'{group_size} companions received {coins_each_companion} coins each.') #