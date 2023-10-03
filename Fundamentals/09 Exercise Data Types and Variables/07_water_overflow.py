numbers_of_rows = int(input())

capacity_tank = 255
total_litters = 0

for rows in range(numbers_of_rows):
    add_litters = int(input())
    if capacity_tank - add_litters < 0 :
        print('Insufficient capacity!')
        continue
    capacity_tank -= add_litters
    total_litters += add_litters

else:
    print(total_litters)





