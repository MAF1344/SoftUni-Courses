budget = float(input())
series = int(input())

cost = 0

for i in range(0, series):
    name = input()
    price = float(input())

    if name == 'Thrones':
        price -= (price * 50/100)
    elif name == 'Lucifer':
        price -= (price * 40/100)
    elif name == 'Protector':
        price -= (price * 30/100)
    elif name == 'TotalDrama':
        price -= (price * 20/100)
    elif name == 'Area':
        price -= (price * 10/100)
    else:
        price = price

    cost += price

if budget >= cost:
    print(f"You bought all the series and left with {budget - cost:.2f} USD.")
else:
    print(f"You need {cost - budget:.2f} USD. more to buy the series!")