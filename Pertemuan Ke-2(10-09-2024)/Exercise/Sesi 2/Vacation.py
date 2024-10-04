money_needed = float(input())
money_available = float(input())

days_counter = 0
spending_counter = 0

while money_available < money_needed and spending_counter < 5:
    command = input()
    money = float(input())
    days_counter += 1  # Increment days_counter

    if command == 'save':
        money_available += money
        spending_counter = 0
    elif command == 'spend':
        money_available -= money
        spending_counter += 1
        if money_available < 0:
            money_available = 0

if spending_counter == 5:
    print("You can't save the money.")
    print(days_counter)
elif money_available >= money_needed:
    print(f"You saved the money for {days_counter} days.")