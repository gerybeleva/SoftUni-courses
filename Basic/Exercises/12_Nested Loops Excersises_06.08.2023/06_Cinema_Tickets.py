console_input = input()
student_qty = 0
standard_qty = 0
kid_qty = 0
total_ticket_counter = 0

while console_input != 'Finish':
    movie_name = console_input
    available_seats = int(input())
    # movie_counter += 1

    ticket_counter = 0
    ticket_type = input()

    while ticket_type != 'End':
        ticket_counter += 1

        if ticket_type == 'student':
            student_qty += 1
        elif ticket_type == 'standard':
            standard_qty += 1
        elif ticket_type == 'kid':
            kid_qty += 1

        if ticket_counter == available_seats:
            break

        ticket_type = input()
    total_ticket_counter += ticket_counter

    perc_tickets_per_movie = ticket_counter / available_seats * 100
    print(f'{movie_name} - {perc_tickets_per_movie:.02f}% full.')
    console_input = input()

print(f'Total tickets: {total_ticket_counter}')
per_total_student_tickets = student_qty / total_ticket_counter * 100
print(f'{per_total_student_tickets:.02f}% student tickets.')
per_total_standard_tickets = standard_qty / total_ticket_counter * 100
print(f'{per_total_standard_tickets:.02f}% standard tickets.')
per_total_kid_tickets = kid_qty / total_ticket_counter * 100
print(f'{per_total_kid_tickets:.02f}% kids tickets.')