total_money = 0

while True:
    destination = input()

    if destination == 'End':
        break

    min_budget = float(input())

    while True:
        money = float(input())
        total_money += money
        if total_money >= min_budget:
            print(f"Going to {destination}!" )
            break

    total_money = 0