import math
from math import floor

current_wr_sec = float(input())
distance_meter = float(input())
swimmer_speed_1m = float(input())

water_resistance_delay = math.floor(distance_meter / 15)
water_resistance_delay_15m = water_resistance_delay * 12.5

total_time_swimmer = distance_meter * swimmer_speed_1m + water_resistance_delay_15m

if total_time_swimmer >= current_wr_sec:
    print(f'No, he failed! He was {total_time_swimmer - current_wr_sec:.02f} seconds slower.')
else:
    print(f'Yes, he succeeded! The new world record is {total_time_swimmer:.02f} seconds.')