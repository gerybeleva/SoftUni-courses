annual_tax = int(input())

sneakers = annual_tax * (1 - 0.4)
outfit = sneakers * (1 - 0.2)
ball = outfit / 4
accessories = ball / 5

total_sum = round(annual_tax + sneakers + outfit + ball + accessories , 2)

print(total_sum)