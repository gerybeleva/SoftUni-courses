budget = float(input())
vc_qty = int(input())
cpu_qty = int(input())
ram_qty = int(input())

vc_price = 250
cpu_price = (vc_qty * vc_price) * 0.35
ram_price = (vc_qty * vc_price) * 0.1

total_expenses = vc_qty * vc_price + cpu_qty * cpu_price + ram_qty * ram_price

if vc_qty > cpu_qty:
    total_expenses = total_expenses * 0.85

if budget >= total_expenses:
    print(f'You have {budget - total_expenses:.02f} leva left!')
else:
    print(f'Not enough money! You need {total_expenses - budget:.02f} leva more!')