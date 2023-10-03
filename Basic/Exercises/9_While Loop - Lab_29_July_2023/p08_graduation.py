student_name = input()

grade = 0
years = 0
not_passed = 0
average_grade = 0

while True:
    current_grade = float(input())
    years += 1

    if 4 <= current_grade <= 6:
        grade += current_grade
        average_grade = grade / years
    if years == 12:
        print(f'{student_name} graduated. Average grade: {average_grade:.02f}')
        break

    elif current_grade < 4:
        not_passed += 1
        if not_passed > 1:
            print(f'{student_name} has been excluded at {years} grade')
            break