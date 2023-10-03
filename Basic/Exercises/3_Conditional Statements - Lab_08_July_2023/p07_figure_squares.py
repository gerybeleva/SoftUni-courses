# square
# rectangle
# circle
# triangle
from math import pi
shape = input()
# side1 = float(input())
# side2 = float(input())

if shape == "square":
    side1 = float(input())
    print(f'{side1**2:.3f}')

elif shape == "rectangle":
    side1 = float(input())
    side2 = float(input())
    print(f'{side1 * side2:.3f}')

elif shape == "circle":
    radius = float(input())
    print(f'{pi * radius**2:.3f}')

elif shape == "triangle":
    a = float(input())
    ha = float(input())
    print(f'{(a * ha) / 2:.3f}')