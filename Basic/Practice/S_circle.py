# This is a program to calculate square of circe in mm2, cm2 and m2.
from math import pi  # import math library

print()  # add a blank row
print("***This is program to calculate the square of the circle.***")  # Print the description ot the Program.
print()  # add a blank row
r = float(input("Input the radius of the circle (cm): "))  # this is input for the circle radius
round_digit = 4  # how many digit left after rounding
S = pi * r ** 2  # calculating the circle square

print(f'S of circle in "mm" is: {round(S * 100, round_digit)} sq. mm')  # Print the S in "mm"
print(f'S of circle in "cm" is: {round(S, round_digit)} sq. cm')  # Print the S in "cm"
print(f'S of circle in "m" is: {round(S / 10000, round_digit)} sq. m')  # Print the S in "m"
