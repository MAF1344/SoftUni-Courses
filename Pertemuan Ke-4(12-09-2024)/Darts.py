name = input()

start_point = 301
leg = 0
failed = 0

while True:
    if start_point == 0:
        break

    field = input()
    if field == 'Retire':
        break

    point = int(input())

    if field == 'Single':
        start_point -= point
        leg += 1
        if start_point < 0:
            start_point += point
            leg -= 1
            failed += 1

    elif field == 'Double':
        start_point -= point * 2
        leg += 1
        if start_point < 0:
            start_point += point * 2
            leg -= 1
            failed += 1

    elif field == 'Triple':
        start_point -= point * 3
        leg += 1
        if start_point < 0:
            start_point += point * 3
            leg -= 1
            failed += 1

    else:
        print("Error")

if start_point == 0:
    print(f"{name} won the leg with {leg} shots.")
else:
    print(f"{name} retired after {failed} unsuccessful shots.")
