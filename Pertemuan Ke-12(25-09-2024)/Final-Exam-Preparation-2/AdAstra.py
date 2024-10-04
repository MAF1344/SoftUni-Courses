def adAstra():
    import re

    pattern = r"([#|])(?P<item>[A-Za-z\s]+)\1(?P<date>\d{2}/\d{2}/\d{2})\1(?P<calories>\d{1,5})\1"
    text = input()

    matches = re.finditer(pattern, text)
    total_calories = 0
    food_items = []

    for match in matches:
        item = match.group("item")
        date = match.group("date")
        calories = int(match.group("calories"))
        total_calories += calories
        food_items.append(f"Item: {item}, Best before: {date}, Nutrition: {calories}")

    days = total_calories // 2000
    print(f"You have food to last you for: {days} days!")
    for item in food_items:
        print(item)

adAstra()