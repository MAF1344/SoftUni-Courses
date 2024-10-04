days_of_stay = int(input())
room_type = input()
grade = input()

nights = days_of_stay - 1

if room_type == "room for one person":
    price_per_night = 18.00
elif room_type == "apartment":
    price_per_night = 25.00
elif room_type == "president apartment":
    price_per_night = 35.00

total_price = nights * price_per_night

if room_type == "apartment":
    if days_of_stay < 10:
        total_price *= 0.70
    elif 10 <= days_of_stay <= 15:
        total_price *= 0.65
    else:
        total_price *= 0.50
elif room_type == "president apartment":
    if days_of_stay < 10:
        total_price *= 0.90
    elif 10 <= days_of_stay <= 15:
        total_price *= 0.85
    else:
        total_price *= 0.80

if grade == "positive":
    total_price *= 1.25
elif grade == "negative":
    total_price *= 0.90

print(f"{total_price:.2f}")
