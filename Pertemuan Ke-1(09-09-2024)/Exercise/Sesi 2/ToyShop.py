trip_price = float(input())
puzzle = int(input())
talking_doll = int(input())
teddy_bear = int(input())
minion = int(input())
truck = int(input())

sold_toys = puzzle + talking_doll + teddy_bear + minion + truck
money_from_toys = (puzzle * 2.60)  + (talking_doll * 3) + (teddy_bear * 4.10) + (minion * 8.20) + (truck * 2)

if sold_toys >= 50:
    money_from_toys *= 0.75

money_left = money_from_toys * 0.90

if money_left >= trip_price:
    print(f"Yes! {money_left - trip_price:.2f} USD left.")
else:
    print(f"Not enough money! {trip_price - money_left:.2f} USD needed.")