
strawberries_price = float(input())
bananas = float(input())
oranges = float(input())
raspberries = float(input())
strawberries = float(input())

raspberries_price = strawberries_price * 1/2
oranges_price = raspberries_price - (raspberries_price * 40/100)
bananas_price = raspberries_price - (raspberries_price * 80/100)

cost = (strawberries_price * strawberries) + (raspberries_price * raspberries) + (oranges_price * oranges) + (bananas_price * bananas)

print(f"{cost:.2f}")