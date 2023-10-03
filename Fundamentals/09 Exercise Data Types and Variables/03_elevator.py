from math import ceil

number_of_persons = int(input())
elevatior_capacity = int(input())

one_line = ceil(number_of_persons / elevatior_capacity) #закръгля нагоре ceil, курсовете са цел. деление + 1
print(one_line)
