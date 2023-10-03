budget = float(input())
season = input() # summer or winter

country = ''  # "Bulgaria", "Balkans" и "Europe"
facility = ''  # "Camp" и "Hotel"
expenses = 0

if budget <= 100:
    country = 'Bulgaria'
    if season == 'summer':
        expenses = budget * 0.3
        facility = 'Camp'
    elif season == 'winter':
        expenses = budget * 0.7
        facility = 'Hotel'

elif budget <= 1000:
    country = 'Balkans'
    if season == 'summer':
        expenses = budget * 0.4
        facility = 'Camp'
    elif season == 'winter':
        expenses = budget * 0.8
        facility = 'Hotel'

elif budget > 1000:
    country = 'Europe'
    expenses = budget * 0.9
    facility = 'Hotel'

print(f"Somewhere in {country}")
print(f"{facility} - {expenses:.02f}")


