product = input()
day = input()
quantity = float(input())

if day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' or day == 'Friday':
    if product == 'banana':
        print(f"{quantity * 2.50:.2f}")
    elif product == 'apple':
        print(f"{quantity * 1.20:.2f}")
    elif product == 'orange':
        print(f"{quantity * 0.85:.2f}")
    elif product == 'grapefruit':
        print(f"{quantity * 1.45:.2f}")
    elif product == 'kiwi':
        print(f"{quantity * 2.70:.2f}")
    elif product == 'pineapple':
        print(f"{quantity * 5.50:.2f}")
    elif product == 'grapes':
        print(f"{quantity * 3.85:.2f}")
    else:
        print("error")
elif day == 'Saturday' or day == 'Sunday':
    if product == 'banana':
        print(f"{quantity * 2.70:.2f}")
    elif product == 'apple':
        print(f"{quantity * 1.25:.2f}")
    elif product == 'orange':
        print(f"{quantity * 0.90:.2f}")
    elif product == 'grapefruit':
        print(f"{quantity * 1.60:.2f}")
    elif product == 'kiwi':
        print(f"{quantity * 3.00:.2f}")
    elif product == 'pineapple':
        print(f"{quantity * 5.60:.2f}")
    elif product == 'grapes':
        print(f"{quantity * 4.20:.2f}")
    else:
        print("error")
else:
    print('error')