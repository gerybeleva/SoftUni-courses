room_w = int(input())
room_l = int(input())
room_h = int(input())
space = room_w * room_l * room_h
box_qty = 0
console_input = input()
diff = 0

while console_input != 'Done':
    if space > box_qty:
        current_boxes = int(console_input)
        box_qty += current_boxes
        diff = abs(space - box_qty)
    if space <= box_qty:
        break

    console_input = input()

if space <= box_qty:
    print(f'No more free space! You need {diff} Cubic meters more.')
else:
    print(f'{diff} Cubic meters left.')