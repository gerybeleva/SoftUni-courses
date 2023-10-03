movie_type = input()
rows = int(input())
columns = int(input())
income = 0
ticket_price = 0

if movie_type == "Premiere":
    ticket_price = 12
    income = ticket_price * rows * columns
elif movie_type == "Normal":
    ticket_price = 7.5
    income = ticket_price * rows * columns
elif movie_type == "Discount":
    ticket_price = 5.0
    income = ticket_price * rows * columns

print(f'{income:.02f} leva')