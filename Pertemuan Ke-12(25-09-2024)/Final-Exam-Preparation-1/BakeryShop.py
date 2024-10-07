foods = {}
foods_count = 0

while True:
    commands = input()
    if commands == "Complete":
        break
    tokens = commands.split()
    command = tokens[0]
    quantity = int(tokens[1])
    food = tokens[2]

    if command == "Receive":
        if quantity <= 0:
            continue
        if food in foods:
            foods[food] += quantity
        else:
            foods[food] = quantity

    elif command == "Sell":
        if food not in foods:
            print(f"You do not have any {food}.")
        else:
            if foods[food] < quantity:
                print(f"There aren't enough {food}. You sold the last {foods[food]} of them.")
                foods_count += foods[food]
                foods[food] = 0
            else:
                foods[food] -= quantity
                foods_count += quantity
                print(f"You sold {quantity} {food}.")

    else:
        print("error")

# Menampilkan sisa stok makanan
for food in foods:
    if foods[food] > 0:
        print(f"{food}: {foods[food]}")

# Menampilkan total barang yang terjual
print(f"All sold: {foods_count} goods")
