cover_price = 1.5
cover_qty = int(input())
paint_price = 14.5
paint_qty = int(input())
thinner_price = 5
thinner_qty = int(input())
bag_price = 0.4

paint_total = paint_qty * 1.1
cover_total = cover_qty + 2

labor_qty = int(input())

sum_materials = round(((cover_price * cover_total) + (paint_price * paint_total) + (thinner_price * thinner_qty)) + bag_price , 2)
labor_price = sum_materials * labor_qty * 0.3

sum_total = sum_materials + labor_price

print(sum_total)
