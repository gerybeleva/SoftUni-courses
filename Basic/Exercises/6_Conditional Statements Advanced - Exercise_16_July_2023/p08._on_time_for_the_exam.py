exam_hour = int(input())
exam_minute = int(input())
arrival_hour = int(input())
arrival_minute = int(input())

exam_time_total_minutes = exam_minute + exam_hour * 60
arrival_time_total_minutes = arrival_minute + arrival_hour * 60
time_diff = abs(exam_time_total_minutes - arrival_time_total_minutes)

if arrival_time_total_minutes > exam_time_total_minutes:
    print('Late')
    if time_diff >= 60:
        hour = time_diff // 60
        minutes = time_diff % 60
        print(f"{hour}:{minutes:02d} hours after the start")
    elif time_diff < 60:
        minutes = time_diff % 60
        print(f"{minutes} minutes after the start")
elif arrival_time_total_minutes == exam_time_total_minutes or time_diff <= 30:
    print('On time')
    if time_diff != 0:
        minutes = time_diff % 60
        print(f"{minutes} minutes before the start")
else:
    print('Early')
    if time_diff >= 60:
        hour = time_diff // 60
        minutes = time_diff % 60
        print(f"{hour}:{minutes:02d} hours before the start")
    elif time_diff < 60:
        minutes = time_diff % 60
        print(f"{minutes} minutes before the start")
