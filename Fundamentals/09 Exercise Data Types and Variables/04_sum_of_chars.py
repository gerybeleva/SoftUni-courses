input_number = int(input())

total_sum = 0
for character in range(input_number):
    input_character = input()
    total_sum += ord(input_character)

print(f"The sum equals: {total_sum}")
