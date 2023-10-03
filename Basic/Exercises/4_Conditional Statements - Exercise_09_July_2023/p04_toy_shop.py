trip_price = float(input())
puzzles_qty = int(input())
dolls_qty = int(input())
tedy_bears_qty = int(input())
minions_qty = int(input())
trucks_qty = int(input())

puzzles_price = 2.6
dolls_price = 3
tedy_bears_price = 4.1
minions_price = 8.2
trucks_price = 2
discount = 25 # 25% discount
rent = 10  # 10% rent from the earned money
total_profit = 0
discounted_price = 0

total_income = (puzzles_qty * puzzles_price + dolls_qty * dolls_price + tedy_bears_qty * tedy_bears_price + minions_qty * minions_price + trucks_qty * trucks_price)
total_qty = (puzzles_qty + dolls_qty + tedy_bears_qty + minions_qty + trucks_qty)

if total_qty >= 50:
    discounted_price = total_income * (1 - discount / 100)
    total_profit = discounted_price - discounted_price * rent / 100
else:
    total_profit = total_income - total_income * rent / 100

if total_profit >= trip_price:
    print(f'Yes! {(total_profit - trip_price):.02f} lv left.')
else:
    print(f'Not enough money! {(trip_price - total_profit):.02f} lv needed.')
