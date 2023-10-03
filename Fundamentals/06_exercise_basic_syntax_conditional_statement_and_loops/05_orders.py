#Gery's file with Gogo's edit :P

order_numbers = int(input())

# price_per_capsule = float(input())
# days = int(input())
# capsules_per_day = int(input())

total_price = 0
coffee_price = 0

for _ in range (order_numbers):
    price_per_capsule = float(input())
    days = int(input())
    capsules_per_day = int(input())

    if not 0 <= price_per_capsule <= 100.00:
        continue
    if not 1 <= days <= 31:
        continue
    if not 1 < capsules_per_day < 2000:
        continue

    coffee_price = price_per_capsule * days * capsules_per_day

    total_price += coffee_price

    if coffee_price != 0:
        print(f'The price for the coffee is: ${coffee_price:.02f}')
if total_price != 0:
    print(f'Total: ${total_price:.02f}')