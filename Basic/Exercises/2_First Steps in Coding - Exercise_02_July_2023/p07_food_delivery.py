chicken_menu = 10.35
chicken_menu_qty = int(input())
fish_menu = 12.40
fish_menu_qty = int(input())
veg_menu = 8.15
veg_menu_qty = int(input())

delivery_service = 2.5

sum_menus = round((chicken_menu * chicken_menu_qty) + (fish_menu * fish_menu_qty) + (veg_menu * veg_menu_qty) , 2)

dessert_cost = sum_menus * 0.2

total_order_price = sum_menus + dessert_cost + delivery_service

print(total_order_price)