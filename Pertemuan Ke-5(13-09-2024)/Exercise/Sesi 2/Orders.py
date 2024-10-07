orders = int(input())
total = 0

for i in range(orders):
    capsule = float(input())
    days = int(input())
    capsules = int(input())

    if not (0.01 <= capsule <= 100.00) or not (1 <= days <= 31) or not (1 <= capsules <= 2000):
        continue

    total_price = capsule * days * capsules
    total += total_price

    print(f"The price for the coffee is: ${total_price:.2f}")

print(f"Total: ${total:.2f}")
