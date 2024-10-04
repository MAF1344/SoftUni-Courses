product = input()
quantity = int(input())

total_price = lambda a, b: a * b

if product == 'coffee':
    print(f"{total_price(quantity, 1.50):.2f}")
elif product == 'water':
    print(f"{total_price(quantity, 1.00):.2f}")
elif product == 'coke':
    print(f"{total_price(quantity, 1.40):.2f}")
elif product == 'snacks':
    print(f"{total_price(quantity, 2.00):.2f}")