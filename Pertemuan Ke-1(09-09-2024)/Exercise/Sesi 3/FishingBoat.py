budget = int(input())
season = input()
fishermen = int(input())

if season == "Spring":
    price = 3000
elif season == 'Summer' or season == 'Autumn':
    price = 4200
elif season == "Winter":
    price = 2600

if fishermen <= 6:
    price *= 0.90
elif 7 <= fishermen <= 11:
    price *= 0.85
else:
    price *= 0.75

if fishermen % 2 == 0 and season != "Autumn":
    price *= 0.95

if budget >= price:
    money_left = budget - price
    print(f"Yes! You have {money_left:.2f} USD left.")
else:
    needed_money = price - budget
    print(f"Not enough money! You need {needed_money:.2f} USD.")
