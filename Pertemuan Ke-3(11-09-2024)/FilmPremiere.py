movie = input()
package = input()
tickets = int(input())

cost = 0

if movie == 'John Wick':
    if package == 'Drink':
        cost += tickets * 12
    elif package == 'Popcorn':
        cost += tickets * 15
    elif package == 'Menu':
        cost += tickets * 19
    else:
        print('Error')
elif movie == 'Star Wars':
    if package == 'Drink':
        cost += tickets * 18
    elif package == 'Popcorn':
        cost += tickets * 25
    elif package == 'Menu':
        cost += tickets * 30
    else:
        print('Error')

    if tickets >= 4:
        cost *= 70/100

elif movie == 'Jumanji':
    if package == 'Drink':
        cost += tickets * 9
    elif package == 'Popcorn':
        cost += tickets * 11
    elif package == 'Menu':
        cost += tickets * 14
    else:
        print('Error')

    if tickets == 2:
        cost *= 85/100

print(f"Your bill is {cost:.2f} USD.")