budget = float(input())
nights = int(input())
price = float(input())
prices = price
additional = budget * int(input()) / 100

if nights > 7:
    price *= 0.95

cost = nights * price + additional

if budget >= cost:
    print(f"Smiths will be left with {budget - cost:.2f} USD after vacation.")
else:
    print(f"{cost - budget:.2f} USD needed.")