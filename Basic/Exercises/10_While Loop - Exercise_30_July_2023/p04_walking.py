target_steps = 10000
total_daily_steps = 0

input_line = input()

while True:
    if input_line == 'Going home':
        input_line = input()
        current_steps = int(input_line)
        total_daily_steps += current_steps
        break

    else:
        current_steps = int(input_line)
        total_daily_steps += current_steps
        if total_daily_steps >= target_steps:
            break

    input_line = input()

step_diff = abs(target_steps - total_daily_steps)
if total_daily_steps >= target_steps:
    print(f'Goal reached! Good job!\n{step_diff} steps over the goal!')

else:
    print(f'{step_diff} more steps to reach goal.')