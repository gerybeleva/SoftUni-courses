# judge 77/100   https://judge.softuni.org/Contests/Compete/Index/2420#2

# input and vars
trip_money = float(input())  # required money for the trip
existing_money = float(input()) # how much money exist at this moment
spend_count = 0  # how many days with spend activities
days_count = 0   # how many Spend / save activities

# calculations
while existing_money < trip_money: # if the existing money are less than trip money enter while cycle
    action = input()  # 'save' or 'spend'
    daily_money = float(input()) # money for the above action

    if existing_money < 0: # if the money goes below 0, zero the amount
        existing_money = 0

    if action == 'save': # in case there is a 'save' activity
        existing_money += daily_money # increase existing money with daily money
        days_count += 1 # increase days count +1
        spend_count = 0 #  This will zero the counter if the activities has changed from Spend to Save

    if action == 'spend': # in case there is a 'spend' activity
        existing_money -= daily_money # decrease the existing money by daily_money
        days_count += 1 # increase days count +1
        spend_count += 1 # increase spend days count +1, this is required to check if we have 5x "spend" in a row
        if spend_count == 5: # if reached 5x spend days - break the cycle
            break

# Print outcome below:
if spend_count == 5:
    print("You can't save the money.")
    print(days_count)

else:
    print(f'You saved the money for {days_count} days.')