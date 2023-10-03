month = input()
stay_days = int(input())

studio_per_night_price = 0
apartment_per_night_price = 0

if month == 'May' or month == 'October':
    studio_per_night_price = 50
    apartment_per_night_price = 65
    if 7 < stay_days <= 14:
        studio_per_night_price = studio_per_night_price * 0.95
    if stay_days > 14:
        studio_per_night_price = studio_per_night_price * 0.7

elif month == 'June' or month == 'September':
    studio_per_night_price = 75.20
    apartment_per_night_price = 68.70
    if  stay_days > 14:
        studio_per_night_price = studio_per_night_price * 0.8

elif month == 'July' or month == 'August':
    studio_per_night_price = 76
    apartment_per_night_price = 77

if stay_days > 14:
    apartment_per_night_price = apartment_per_night_price * 0.9

total_apartment_price = apartment_per_night_price * stay_days
total_studio_price = studio_per_night_price * stay_days


print(f'Apartment: {total_apartment_price:.02f} lv.')
print(f'Studio: {total_studio_price:.02f} lv.')
