input_lines = int(input())
comp_word = input()

new_string = []

for _ in range(input_lines):
    input_string = input()
    new_string.append(input_string)
print(new_string)

filtered_string = []

for string in new_string:
    if comp_word in string:
        filtered_string.append(string)
print(filtered_string)