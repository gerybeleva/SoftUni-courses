evaluators = int(input())
presentation_name = input()

count_all_grades = 0
sum_all_grades = 0

while presentation_name != 'Finish':

    presentation_grade = 0
    presentation_count = 0
    for i in range(1, evaluators + 1):
        grade = float(input())
        presentation_grade += grade
        presentation_count += 1
        sum_all_grades += grade
        count_all_grades += 1

    print(f'{presentation_name} - {(presentation_grade / presentation_count):.02f}.')

    presentation_name = input()

avr_exam = sum_all_grades / count_all_grades
print(f"Student's final assessment is {avr_exam:.02f}.")
