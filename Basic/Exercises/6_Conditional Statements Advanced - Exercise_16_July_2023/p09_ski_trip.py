
stay_days = int(input())
room_type = input() # "room for one person", "apartment" , "president apartment"
review = input() #  "positive" , "negative"
stay_nights = stay_days - 1

room_price = 0

if stay_days < 10:
    if room_type == 'room for one person':
        room_price = 18
    elif room_type == 'apartment':
        room_price = 25 * 0.7
    elif room_type == 'president apartment':
        room_price = 35 * 0.9
elif 10 <= stay_days <= 15:
    if room_type == 'room for one person':
        room_price = 18
    elif room_type == 'apartment':
        room_price = 25 * 0.65
    elif room_type == 'president apartment':
        room_price = 35 * 0.85
else:
    if room_type == 'room for one person':
        room_price = 18
    elif room_type == 'apartment':
        room_price = 25 * 0.5
    elif room_type == 'president apartment':
        room_price = 35 * 0.8

if review == 'positive':
    total = room_price * stay_nights * 1.25
    print(f'{total:.02f}')
else:
    total = room_price * stay_nights * 0.9
    print(f'{total:.02f}')