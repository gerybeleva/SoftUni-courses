count_number = int(input())

for _ in range (count_number):
    number = int(input())

    if number % 2 != 0:
        print(f'{number} is odd!')
        break
else:
    print('All numbers are even.')
