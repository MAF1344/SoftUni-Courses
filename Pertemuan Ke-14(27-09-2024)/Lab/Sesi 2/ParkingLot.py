car_count = int(input())
parking_lot = set()

for _ in range(car_count):
    direction, plate_number = input().split(", ")
    if direction == "IN":
        parking_lot.add(plate_number)
    elif direction == "OUT":
        parking_lot.discard(plate_number)

if parking_lot:
    print("\n".join(parking_lot))
else:
    print("Parking Lot is Empty")