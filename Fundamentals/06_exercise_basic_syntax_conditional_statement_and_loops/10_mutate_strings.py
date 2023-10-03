first_str = input()
second_str = input()

new_string = ""

if len(first_str) == len(second_str):

    new_string = second_str.replace(character(first_str), character(second_str))
    print(new_string)



else:
    break