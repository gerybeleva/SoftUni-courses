import math
from math import ceil

name = input()
movie_duration = int(input())
break_duration = int(input())

lunch_time = break_duration / 8
rest_time = break_duration / 4

time_left = break_duration - lunch_time - rest_time

if movie_duration <= time_left:
    print(f'You have enough time to watch {name} and left with {math.ceil(time_left - movie_duration)} minutes free time.')
else:
    print(f"You don't have enough time to watch {name}, you need {math.ceil(movie_duration - time_left)} more minutes.")