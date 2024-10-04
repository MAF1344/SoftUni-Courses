orders = {}

while True:
    command = input().strip()
    if command == "buy":
        break
    tokens = command.split()
    product = tokens[0]
    price = float(tokens[1])
    quantity = int(tokens[2])

    if product in orders:
        current_price, current_quantity = orders[product]
        orders[product] = (price, current_quantity + quantity)
    else:
        orders[product] = (price, quantity)

for product, (price, quantity) in orders.items():
    total_price = price * quantity
    print(f"{product} -> {total_price:.2f}")