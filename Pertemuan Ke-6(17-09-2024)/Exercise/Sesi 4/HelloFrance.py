items = input().split("|")
budget = float(input())

bought_items = []
profit = 0

max_price = {
    "Clothes": 50.00,
    "Shoes": 35.00,
    "Accessories": 20.50
}

for item in items:
    item_type, price = item.split("->")
    price = float(price)

    if price <= max_price.get(item_type, 0) and budget >= price:
        budget -= price
        bought_items.append(price * 1.40)
        profit += price * 0.40

new_budget = budget + sum(bought_items)
print(" ".join(f"{item:.2f}" for item in bought_items))
print(f"Profit: {profit:.2f}")

if new_budget >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")