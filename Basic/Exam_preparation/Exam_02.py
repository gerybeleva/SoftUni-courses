days = 5
daily_money = float(input())
daily_sells = float(input())
total_expenses = float(input())
gift_price = float(input())

total_imcome = days *( daily_money + daily_sells)
profit = total_imcome - total_expenses

if profit >= gift_price:
    print(f'Profit: {profit:.02f} BGN, the gift has been purchased.')

else:
    diff = abs(profit - gift_price)
    print(f'Insufficient money: {diff:.02f} BGN.')
