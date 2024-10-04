budget = float(input())

cost = 0

while True:
    if budget < 0:
        break

    actor = input()

    if actor == 'ACTION':
        break
    elif len(actor) > 15:
        salary = budget * 20 / 100
        cost += salary
        budget -= salary
    else:
        salary = float(input())
        cost += salary
        budget -= salary

if budget >= 0:
    print(f"We are left with {budget:.2f} USD.")
else:
    print(f"We need {abs(budget):.2f} USD for our actors.")