open_tabs = int(input())
salary = int(input())

for _ in range(open_tabs):
    web_site = input()
    if web_site == 'Facebook':
        salary -= 150
    elif web_site == 'Instagram':
        salary -= 100
    elif web_site == 'Reddit':
        salary -= 50

    if salary <= 0:
        print(f'You have lost your salary.')
        break

if salary > 0:
    print(salary)

