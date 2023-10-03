book = input()
library_books = 0
checked_books = 0

while True:

    library_books = input()
    checked_books += 1

    if book == library_books:
        checked_books -= 1
        print(f'You checked {checked_books} books and found it.')
        break

    if library_books == 'No More Books':
        checked_books -= 1
        print('The book you search is not here!')
        print(f'You checked {checked_books} books.')
        break