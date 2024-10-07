depo = input()
balance = 0.0

while depo != "NoMoreMoney":
    amount = float(depo)
    if amount < 0:
        print("Invalid operation!")
        break

    balance += amount
    print(f"Increase: {amount:.2f}")
    depo = input()

print(f"Total: {balance:.2f}")
