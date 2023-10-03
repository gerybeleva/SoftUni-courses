import math
from math import floor
tournament_count = int(input())
ranglist_points = int(input())

total_points = ranglist_points
total_wons = 0

for _ in range(tournament_count):
    tournament_position = input()
    if tournament_position == 'W':
        total_points += 2000
        total_wons += 1
    elif tournament_position == 'F':
        total_points += 1200
    elif tournament_position == 'SF':
        total_points += 720

average_points = math.floor((total_points - ranglist_points) / tournament_count)
percent_wons = total_wons / tournament_count * 100

print(f'Final points: {total_points}')
print(f'Average points: {average_points}')
print(f'{percent_wons:.02f}%')
