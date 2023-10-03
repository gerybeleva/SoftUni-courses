budjet = int(input())
command = input()

while command != 'End':
    product_price = int(command)
    budjet -= product_price
    if budjet < 0:
        print('You went in overdraft!')
        break
    command = input()
else:
    print('You bought everything needed.')

