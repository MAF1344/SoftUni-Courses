budget = float(input())
destination = input()
season = input()
days = int(input())
cost = 0

if season == 'Winter':
    if destination == 'Dubai':
        pay = days * 45000
        cost += pay
        cost = cost - (cost * 30/100)
    elif destination == 'Washington':
        pay = days * 17000
        cost += pay
        cost = cost + (cost * 25 / 100)
    elif destination == 'London':
        pay = days * 24000
        cost += pay
    else:
        print('Error')
elif season == 'Summer':
    if destination == 'Dubai':
        pay = days * 40000
        cost += pay
        cost = cost - (cost * 30/100)
    elif destination == 'Washington':
        pay = days * 12500
        cost += pay
        cost = cost + (cost * 25 / 100)
    elif destination == 'London':
        pay = days * 20250
        cost += pay
    else:
        print('Error')
else:
    print('Error')

if budget > cost:
    print(f"The budget for the movie is enough! We have {budget - cost:.2f} USD left!")
else:
    print(f"The director needs {cost - budget:.2f} USD more!")