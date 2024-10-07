money = list(map(int, input().split()))
prices = list(map(int, input().split()))
eat_food = 0
food_skipped = 0

money = money[::-1]

while money and prices:
    current_money = money[0]
    current_price = prices[0]

    if current_money == current_price:
        money.pop(0)
        prices.pop(0)
        eat_food += 1
    elif current_money > current_price:
        change = current_money - current_price
        money.pop(0)
        prices.pop(0)
        if money:
            money[0] += change
        eat_food += 1
    else:
        money.pop(0)
        prices.pop(0)
        food_skipped += 1

if eat_food == 0:
    print("Henry remained hungry. He will try next weekend again.")
elif eat_food == 1:
    print(f"Henry ate: {eat_food} food.")
elif food_skipped == 0:
    print(f"Gluttony of the day! Henry ate {eat_food} foods.")
else:
    print(f"Henry ate: {eat_food} foods.")
