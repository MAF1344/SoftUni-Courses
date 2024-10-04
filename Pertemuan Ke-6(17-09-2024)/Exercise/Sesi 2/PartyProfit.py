group_size = int(input())
days = int(input())

coins_earned = 0

for day in range(1, days + 1):
    coins_daily = 0
    coins_daily += 50

    if day % 10 == 0:
        group_size -= 2

    if day % 15 == 0:
        group_size += 5

    coins_daily -= 2 * group_size

    if day % 3 == 0:
        coins_daily -= 3 * group_size

    if day % 5 == 0:
        coins_daily += 20 * group_size
        if day % 3 == 0:
            coins_daily -= 2 * group_size

    coins_earned += coins_daily

if group_size > 0:
    coins_per_companion = coins_earned // group_size
else:
    coins_per_companion = 0

print(f"{group_size} companions received {coins_per_companion} coins each.")