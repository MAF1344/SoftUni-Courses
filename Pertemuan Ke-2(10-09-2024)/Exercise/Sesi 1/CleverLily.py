age = int(input())
washing_machine = float(input())
toy_price = int(input())
count_toy = 0
money_saved = 0
birthday_money = 0

for i in range(1, age + 1):
    if i % 2 == 0:
        birthday_money += 10
        money_saved += birthday_money - 1
    else:
        count_toy += 1

money_saved += count_toy * toy_price

if money_saved >= washing_machine:
    print(f"Yes! {money_saved - washing_machine:.2f}")
else:
    print(f"No! {washing_machine - money_saved:.2f}")
