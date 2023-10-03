flower_type = input()
flower_qty = int(input())
budget = float(input())

flower_price = 0
total_cost = 0

if flower_type == "Roses":
    flower_price = 5
    total_cost = flower_qty * flower_price
    if flower_qty > 80:
        total_cost = total_cost * 0.9
elif flower_type == "Dahlias":
    flower_price = 3.8
    total_cost = flower_qty * flower_price
    if flower_qty > 90:
        total_cost = total_cost * 0.85
elif flower_type == "Tulips":
    flower_price = 2.8
    total_cost = flower_qty * flower_price
    if flower_qty > 80:
        total_cost = total_cost * 0.85
elif flower_type == "Narcissus":
    flower_price = 3.0
    total_cost = flower_qty * flower_price
    if flower_qty < 120:
        total_cost = total_cost * 1.15
elif flower_type == "Gladiolus":
    flower_price = 2.5
    total_cost = flower_qty * flower_price
    if flower_qty < 80:
        total_cost = total_cost * 1.2

remaining_amount = abs(budget - total_cost)

if budget >= total_cost:
    print(f"Hey, you have a great garden with {flower_qty} {flower_type} and {remaining_amount:.02f} leva left.")
else:
    print(f"Not enough money, you need {remaining_amount:.02f} leva more.")