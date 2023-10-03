destination = input()
money = 0

while destination != 'End':
    cost = float(input())
    while True:
        add_money = input()
        money += float(add_money)
        if money >= cost:
            print(f'Going to {destination}!')
            money = 0
            break
    destination = input()