enter_n = int(input())

i=0

for i in range(enter_n):
    number = int(input())
    if number == 88:
        print('Hello')
    elif number == 86:
        print('How are you?')
    elif number <88:
        print('GREAT!')
    else:
        print('Bye.')
    i +=1