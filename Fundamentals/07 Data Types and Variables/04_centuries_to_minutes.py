insert_centuries = int(input())

years = insert_centuries * 100
days = int(years * 365.2422)
hours = abs(days * 24)
minutes = hours * 60
#centuries and converts it to years, days, hours, and minutes.

print(f'{insert_centuries} centuries = {years} years = {days} days = {hours} hours = {minutes} minutes')