product = input()
city = input()
quantity = float(input())
price = 0

if city == 'London':
    if product == 'coffee':
        price = 0.50
    elif product == 'water':
        price = 0.80
    elif product == 'beer':
        price = 1.20
    elif product == 'sweets':
        price = 1.45
    elif product == 'peanuts':
        price = 1.60
    else:
        print("Product Doesn't Exist")
elif city == 'Rome':
    if product == 'coffee':
        price = 0.40
    elif product == 'water':
        price = 0.70
    elif product == 'beer':
        price = 1.15
    elif product == 'sweets':
        price = 1.30
    elif product == 'peanuts':
        price = 1.50
    else:
        print("Product Doesn't Exist")
elif city == 'Paris':
    if product == 'coffee':
        price = 0.45
    elif product == 'water':
        price = 0.70
    elif product == 'beer':
        price = 1.10
    elif product == 'sweets':
        price = 1.35
    elif product == 'peanuts':
        price = 1.55
    else:
        print("Product Doesn't Exist")
else:
    print("City Doesn't Exist")



print(round((quantity * price),4))