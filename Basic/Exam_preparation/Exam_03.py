single_room_price = 18
apartment_price = 25
president_price = 35

days_of_stay = int(input())
nights = days_of_stay - 1
room_type = input()
review = input()
total_price = 0
final_payment = 0

if days_of_stay < 10:
    if room_type == 'room for one person':
        total_price = nights * single_room_price
    elif room_type == 'apartment':
        total_price = nights * apartment_price
        final_payment = total_price * 0.7
    elif room_type == 'president apartment':
        total_price = nights * president_price
        final_payment = total_price * 0.9

elif 10 < days_of_stay <= 15:
    if room_type == 'room for one person':
        total_price = nights * single_room_price
    elif room_type == 'apartment':
        total_price = nights * apartment_price
        final_payment = total_price * 0.65
    elif room_type == 'president apartment':
        total_price = nights * president_price
        final_payment = total_price * 0.85
else:
    if room_type == 'room for one person':
        total_price = nights * single_room_price
    elif room_type == 'apartment':
        total_price = nights * apartment_price
        final_payment = total_price * 0.5
    elif room_type == 'president apartment':
        total_price = nights * president_price
        final_payment = total_price * 0.8

if review == 'positive':
    final_payment = final_payment * 1.25
    print(f'{final_payment:.02f}')
if review == 'negative':
    final_payment = final_payment * 0.9
    print(f'{final_payment:.02f}')