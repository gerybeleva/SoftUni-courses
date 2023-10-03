number_lines = int(input())

positive_numbers = []
negative_numbers = []

for numbers in range(number_lines):
    input_number = int(input())
    if input_number >= 0:
        positive_numbers.append(input_number)
    else:
        negative_numbers.append(input_number)

print(positive_numbers)
print(negative_numbers)
print("Count of positives:", len(positive_numbers))
print("Sum of negatives:", sum(negative_numbers))

