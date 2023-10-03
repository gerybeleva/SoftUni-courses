cake_width = int(input())
cake_lenght = int(input())
total_cake_pcs = cake_lenght * cake_width
remaining_pcs = total_cake_pcs
diff = 0

console_input = input()

while console_input != 'STOP':
    if total_cake_pcs >= 0:
        piece_take = int(console_input)
        remaining_pcs -= piece_take

    if remaining_pcs < 0:
        diff = abs(remaining_pcs)
        break
    console_input = input()

if console_input != 'STOP':
    print(f'No more cake left! You need {diff} pieces more.')
else:
    print(f'{remaining_pcs} pieces are left.')