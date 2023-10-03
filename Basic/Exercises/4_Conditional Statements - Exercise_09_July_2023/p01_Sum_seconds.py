first_sec = int(input())
second_sec = int(input())
third_sec = int(input())

total_seconds = first_sec + second_sec + third_sec

minutes = total_seconds // 60
seconds = total_seconds % 60

print(f'{minutes}:{seconds:02}')