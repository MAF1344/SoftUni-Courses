budget = float(input())
decor = budget * (10/100)
extra = int(input())
clothing = float(input()) * extra

if extra >= 150:
    clothing = clothing - (clothing * (10/100))

cost = decor + clothing

if budget >= cost:
    print(f"Action!")
    print(f"Wingard starts filming with {budget - cost:.2f} USD left.")
else:
    print(f"Not enough money!")
    print(f"Wingard needs {cost - budget:.2f} USD more.")