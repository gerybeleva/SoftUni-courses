# Write a program that reads an integer number of centuries and converts it to years, days, hours, and minutes.
# Assume that one year has 365.2422 days on average
import math
from math import floor

centuries = int(input())
days_per_year = 365.2422  # Need to format the number to 2 digits after decimal.


years = centuries * 100
days = math.floor(years * days_per_year)
hours = days * 24
minutes = hours * 60
format_number = 0

#print(f'{centuries} -- {years} -- {days} -- {hours} -- {minutes}' )
#print(f'{centuries} centuries = {years:.{format_number}f} years = {days:.{format_number}f} days = {hours:.{format_number}f} hours = {minutes:.{format_number}f} minutes')
print(f'{centuries} centuries = {years} years = {days} days = {hours} hours = {minutes} minutes')