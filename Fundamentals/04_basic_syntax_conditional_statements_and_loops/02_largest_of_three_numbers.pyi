number_a = int(input())
number_b = int(input())
number_c = int(input())

max_number = 0

if number_a > number_b:
    max_number = number_a
elif number_b > number_c:
    max_number = number_b
else:
    max_number = number_c

print(max_number)
