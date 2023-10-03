hours = int(input())
minutes = int(input())

hours_to_minutes = hours * 60
current_time_min = hours_to_minutes + minutes
new_time = current_time_min + 15

if 0 <= hours <= 23 and 0 <= minutes <= 59:
    new_hours = new_time // 60
    new_minutes = new_time % 60
    if new_hours > 23:
        new_hours = 0

    print(f'{new_hours}:{new_minutes:02}')