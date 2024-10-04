budget = float(input())
season = input()

if budget <= 100:
    destination = "Somewhere in Bulgaria"
    if season == "summer":
        cost = 0.30 * budget
        accommodation = "Camp"
    else:
        cost = 0.70 * budget
        accommodation = "Hotel"
elif budget <= 1000:
    destination = "Somewhere in Balkans"
    if season == "summer":
        cost = 0.40 * budget
        accommodation = "Camp"
    else:
        cost = 0.80 * budget
        accommodation = "Hotel"
else:
    destination = "Somewhere in Europe"
    cost = 0.90 * budget
    accommodation = "Hotel"

print(f"{destination}")
print(f"{accommodation} - {cost:.2f}")