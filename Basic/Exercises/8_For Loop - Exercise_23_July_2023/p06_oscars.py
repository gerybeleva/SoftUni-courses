actor_name = input()
academy_points = float(input())
voting_number = int(input())

for _ in range(voting_number):
    evaluating_person = input()
    eval_points = float(input())
    academy_points += (len(evaluating_person) * eval_points) / 2

    if academy_points > 1250.5:
        print(f'Congratulations, {actor_name} got a nominee for leading role with {academy_points:.01f}!')
        break
else:
    diff = 1250.5 - academy_points
    print(f'Sorry, {actor_name} you need {diff:.01f} more!')

# evaluating_person = input()
# lenght = len(evaluating_person)
# print(lenght)