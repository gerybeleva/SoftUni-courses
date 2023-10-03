budget = float(input())
stage_crew_qty = int(input())
stage_costume_price = float(input())

decor = budget * 0.1
costume_discount = 0.1 # 10% costumes discount. MOQ = 150

expenses_costumes = stage_crew_qty * stage_costume_price
total_expenses = expenses_costumes + decor



if stage_crew_qty > 150:
    total_expenses = expenses_costumes * 0.9 + decor
else:
    total_expenses = total_expenses

if total_expenses <= budget:
    print(f'Action!')
    print(f'Wingard starts filming with {budget - total_expenses:.02f} leva left.')
else:
    print("Not enough money!")
    print(f'Wingard needs {total_expenses - budget:.02f} leva more.')