greening_surface = float(input())
greening_price = 7.61
discount = 18/100

greening_price = greening_surface * greening_price
discounted_price = greening_price * discount
final_price = greening_price - discounted_price

print(f'The final price is: {final_price} lv.')
print(f'the discount is: {discounted_price} lv')