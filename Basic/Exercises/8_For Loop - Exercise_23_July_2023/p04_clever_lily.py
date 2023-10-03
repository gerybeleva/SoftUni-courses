age = int(input())
washing_mashine = float(input())
toy = int(input())

money = 0
money_increment = 0
money_toy = 0
total_money = 0

for bd in range(1, age + 1):
    if bd % 2 != 0:
        money_toy += toy
    else:
        money_increment += 10
        money += money_increment
        money -= 1

total_money = money_toy + money

# print(total_money)

diff = abs(total_money - washing_mashine)

if total_money >= washing_mashine:
    print(f'Yes! {diff:.02f}')
else:
    print(f'No! {diff:.02f}')