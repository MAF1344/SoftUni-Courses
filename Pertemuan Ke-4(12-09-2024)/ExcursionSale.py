sea = int(input())
mountain = int(input())

profit = 0

while True:
    if sea == 0 and mountain == 0:
        break

    package = input()

    if package == 'Stop':
        break
    elif sea == 0 and package == 'sea':
        print('')
    elif mountain == 0 and package == 'mountain':
        print('')
    else:
        if package == 'sea':
            sea -= 1
            profit += 680
        elif package == 'mountain':
            mountain -= 1
            profit += 499
        else:
            print('Error')

if sea == 0 and mountain == 0:
    print("Good job! Everything is sold." )

print(f"Profit: {profit} USD.")