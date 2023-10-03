console_input = input()

total_goals = 0
best_player = ''

while console_input != 'END':
    player_name = console_input
    goals = int(input())
    if goals > total_goals:
        total_goals = goals
        best_player = player_name
    if goals >= 10:
        break
    console_input = input()

print(f'{best_player} is the best player!')

if total_goals >= 3:
    print(f'He has scored {total_goals} goals and made a hat-trick !!!')
else:
    print(f'He has scored {total_goals} goals.')