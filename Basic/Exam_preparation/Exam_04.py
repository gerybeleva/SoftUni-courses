from math import *
training_days = int(input())
initial_day_distance = float(input())
km_days = initial_day_distance
days_counter = 1
daily_percent_increase = int(input())
total_km = initial_day_distance

while total_km < 1000:
    km_days =  km_days + km_days * (daily_percent_increase / 100)
    total_km += km_days

    if days_counter == training_days:
        break
    days_counter += 1
    daily_percent_increase = int(input())

diff_km = ceil(abs(1000 - total_km))

if total_km >= 1000:
    print(f"You've done a great job running {diff_km} more kilometers!")
else:
    print(f'Sorry Mrs. Ivanova, you need to run {diff_km} more kilometers')