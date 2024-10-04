flower = input()
flower_amount = int(input())
budget = int(input())
final_cost = 0

if flower == 'Roses':
    cost = flower_amount * 5
    if flower_amount > 80:
        final_cost = cost * 0.90
    else:
        final_cost = cost
elif flower == 'Dahlias':
    cost = flower_amount * 3.80
    if flower_amount > 90:
        final_cost = cost * 0.85
    else:
        final_cost = cost
elif flower == 'Tulips':
    cost = flower_amount * 2.80
    if flower_amount > 80:
        final_cost = cost * 0.85
    else:
        final_cost = cost
elif flower == 'Narcissus':
    cost = flower_amount * 3
    if flower_amount < 120:
        final_cost = cost * 1.15
    else:
        final_cost = cost
elif flower == 'Gladiolus':
    cost = flower_amount * 2.50
    if flower_amount < 80:
        final_cost = cost * 1.20
    else:
        final_cost = cost

if budget >= final_cost:
    print(f"Hey, you have a great garden with {flower_amount} {flower} and {budget - final_cost:.2f} USD left.")
else:
    print(f"Not enough money, you need {final_cost - budget:.2f} USD more.")