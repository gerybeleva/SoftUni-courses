#Write a program that reads an integer n. Then, for all numbers in the range [1, n],
# prints the number and if it is special or not (True / False). A number is special when the sum of its digits is 5, 7, or 11

input_number = int(input())

for number in range(1, input_number + 1):
    current_number = str(number)
    digit_sum = 0
    for digit in current_number:
        digit_sum += int(digit)

    if (digit_sum == 5) or (digit_sum == 7) or (digit_sum == 11):
        print(f'{number} -> True')
    else:
        print(f'{number} -> False')