lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

total_expenses = 0
broken_shields = 0

for fight in range(1, lost_fights + 1):
    if fight % 2 == 0:
        total_expenses += helmet_price
    if fight % 3 == 0:
        total_expenses += sword_price
    if fight % 2 == 0 and fight % 3 == 0:
        total_expenses += shield_price
        broken_shields += 1
        if broken_shields % 2 == 0:
            total_expenses += armor_price

print(f"Gladiator expenses: {total_expenses:.2f} aureus")