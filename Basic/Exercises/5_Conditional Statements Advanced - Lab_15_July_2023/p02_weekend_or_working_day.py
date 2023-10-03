
week_day = input()

if week_day == 'Monday' or week_day == 'Tuesday' or week_day == 'Wednesday' \
        or week_day == 'Thursday' or week_day == 'Friday' \
        or week_day == 'Saturday' or week_day == 'Sunday':
    if week_day == 'Monday':
        print("Working day")
    elif week_day == 'Tuesday':
        print("Working day")
    elif week_day == 'Wednesday':
        print("Working day")
    elif week_day == 'Thursday':
        print("Working day")
    elif week_day == 'Friday':
        print("Working day")
    elif week_day == 'Saturday':
        print("Weekend")
    elif week_day == 'Sunday':
        print("Weekend")
else:
    print("Error")
