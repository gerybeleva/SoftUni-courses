unsuficient_grade_qty = int(input())

grade_counter = 0
count_poor = 0
sum_grade = 0
last_task_name = ''
failed = False
average_grade = 0

task_name = input()

while task_name != 'Enough':
    current_grade = int(input())
    if current_grade <= 4:
        count_poor += 1
    if count_poor == unsuficient_grade_qty:
        failed = True
        break
    grade_counter += 1
    sum_grade += current_grade
    last_task_name = task_name
    task_name = input()
    if task_name == 'Enough':
        break
average_grade = sum_grade / grade_counter

if failed:
    print(f'You need a break, {count_poor} poor grades.')
else:
    print(f"Average score: {average_grade:.02f}")
    print(f"Number of problems: {grade_counter}")
    print(f"Last problem: {last_task_name}")
