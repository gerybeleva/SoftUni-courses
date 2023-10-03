book_pages = int(input())
pages_per_hour = int(input())
days = int(input())

time_required = book_pages // pages_per_hour
hours = time_required / days

print(hours)
