enter_name = input()

while enter_name != "Welcome!":
    if enter_name == "Voldemort":
        print('You must not speak of that name!')
        break
    elif len(enter_name) < 5:
        print(f"{enter_name} goes to Gryffindor.")
    elif len(enter_name) == 5:
        print(f"{enter_name} goes to Slytherin.")
    elif len(enter_name) == 6:
        print(f"{enter_name} goes to Ravenclaw.")
    elif len(enter_name) > 6:
        print(f"{enter_name} goes to Hufflepuff.")

    enter_name = input()
else:
    print(f'Welcome to Hogwarts.')