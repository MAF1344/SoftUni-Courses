def price_counter():
    total_price = 0
    total_tax = 0
    cost = 0

    while True:
        price = input()
        if price == 'special':
            cost = (total_price + total_tax) * 90/100
            break
        elif price == 'regular':
            break

        if float(price) < 0:
            print("Invalid price!")
            continue

        price = float(price)
        total_price += price
        total_tax += price * 20/100
        cost += (price + (price * 20/100))

    if cost == 0:
        print( "Invalid order!")
    else:
        print("Congratulations you've just bought a new computer!")
        print(f"Price without taxes: ${total_price:.2f}")
        print(f"Taxes: ${total_tax:.2f}")
        print("-----------")
        print(f"Total price: ${cost:.2f}")

price_counter()