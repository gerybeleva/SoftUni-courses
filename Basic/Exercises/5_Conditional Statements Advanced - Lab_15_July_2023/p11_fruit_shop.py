# fruit = banana / apple / orange / grapefruit / kiwi / pineapple / grapes;
# week day = Monday / Tuesday / Wednesday / Thursday / Friday / Saturday / Sunday;

fruit = input()
week_day = input()
fruit_qty = float(input())

banana_price = 0
apple_price = 0
orange_price = 0
grapefruit_price = 0
kiwi_price = 0
pineapple_price = 0
grapes_price = 0
total_price = 0

if (week_day == "Monday" \
    or week_day == "Tuesday" \
    or week_day == "Wednesday" \
    or week_day == "Thursday" \
    or week_day == "Friday") \
    and  (fruit == "banana" \
    or fruit == "apple"  \
    or fruit == "orange" \
    or fruit == "grapefruit" \
    or fruit == "kiwi" \
    or fruit == "pineapple" \
    or fruit == "grapes"):
    banana_price = 2.5
    apple_price = 1.2
    orange_price = 0.85
    grapefruit_price = 1.45
    kiwi_price = 2.70
    pineapple_price = 5.50
    grapes_price = 3.85
    if fruit == "banana":
        total_price = fruit_qty * banana_price
    elif fruit == "apple":
        total_price = fruit_qty * apple_price
    elif fruit == "orange":
        total_price = fruit_qty * orange_price
    elif fruit == "grapefruit":
        total_price = fruit_qty * grapefruit_price
    elif fruit == "kiwi":
        total_price = fruit_qty * kiwi_price
    elif fruit == "pineapple":
        total_price = fruit_qty * pineapple_price
    elif fruit == "grapes":
        total_price = fruit_qty * grapes_price
    print(f'{total_price:.02f}')
elif (week_day == "Saturday" \
    or week_day == "Sunday") \
    and  (fruit == "banana" \
    or fruit == "apple"  \
    or fruit == "orange" \
    or fruit == "grapefruit" \
    or fruit == "kiwi" \
    or fruit == "pineapple" \
    or fruit == "grapes"):
    banana_price = 2.7
    apple_price = 1.25
    orange_price = 0.90
    grapefruit_price = 1.60
    kiwi_price = 3.00
    pineapple_price = 5.60
    grapes_price = 4.20
    if fruit == "banana":
        total_price = fruit_qty * banana_price
    elif fruit == "apple":
        total_price = fruit_qty * apple_price
    elif fruit == "orange":
        total_price = fruit_qty * orange_price
    elif fruit == "grapefruit":
        total_price = fruit_qty * grapefruit_price
    elif fruit == "kiwi":
        total_price = fruit_qty * kiwi_price
    elif fruit == "pineapple":
        total_price = fruit_qty * pineapple_price
    elif fruit == "grapes":
        total_price = fruit_qty * grapes_price
    print(f'{total_price:.02f}')
else:
    print("error")