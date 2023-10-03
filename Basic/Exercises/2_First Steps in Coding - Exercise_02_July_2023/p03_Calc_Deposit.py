deposit_amount = float(input())
months = int(input())
annual_rate = float(input())

# per_year = deposit_amount * (annual_rate/100)

final_amount = deposit_amount + (months * ((deposit_amount * (annual_rate / 100) / 12)))

print(final_amount)