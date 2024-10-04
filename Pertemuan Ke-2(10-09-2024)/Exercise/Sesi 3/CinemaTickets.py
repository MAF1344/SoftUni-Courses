ticket_sold = 0
student = 0
standard = 0
kid = 0

while True:
    movie_title = input()

    if movie_title == 'Finish':
        break

    seats = int(input())
    seat = 0

    for i in range(0, seats):
        customer = input()
        if customer == 'End':
            break
        elif i >= seats:
            break
        elif customer == 'student':
            student += 1
            seat += 1
            ticket_sold += 1
        elif customer == 'standard':
            standard += 1
            seat += 1
            ticket_sold += 1
        elif customer == 'kid':
            kid += 1
            seat += 1
            ticket_sold += 1

    print(f"{movie_title} - {seat / seats * 100:.2f}% full.")

print(f"Total tickets: {ticket_sold}")
print(f"{student / ticket_sold * 100:.2f}% student tickets.")
print(f"{standard / ticket_sold * 100:.2f}% standard tickets.")
print(f"{kid / ticket_sold * 100:.2f}% kids tickets.")