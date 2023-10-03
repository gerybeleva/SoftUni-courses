zoo_list = []

for _ in range (3):
    input_zoo = input()
    zoo_list.append(input_zoo)

zoo_list[0], zoo_list[2] = zoo_list[2], zoo_list[0]
print(zoo_list)