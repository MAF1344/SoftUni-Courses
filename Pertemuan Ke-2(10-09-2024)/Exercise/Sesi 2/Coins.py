change = float(input())
change = int(change * 100)

coins_count = 0

while change > 0:
    if change >= 200:  # 2.00 EUR
        change -= 200
    elif change >= 100:  # 1.00 EUR
        change -= 100
    elif change >= 50:  # 0.50 EUR
        change -= 50
    elif change >= 20:  # 0.20 EUR
        change -= 20
    elif change >= 10:  # 0.10 EUR
        change -= 10
    elif change >= 5:  # 0.05 EUR
        change -= 5
    elif change >= 2:  # 0.02 EUR
        change -= 2
    elif change >= 1:  # 0.01 EUR
        change -= 1
    coins_count += 1

print(coins_count)
