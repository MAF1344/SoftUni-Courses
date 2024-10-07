n = int(input())
filled_tank = 0

for i in range(n):
    pour = int(input())
    filled_tank += pour

    if filled_tank > 255:
        print("Insufficient capacity!")
        filled_tank -= pour

print(filled_tank)