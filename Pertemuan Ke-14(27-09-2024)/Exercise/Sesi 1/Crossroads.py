from collections import deque

green_light = int(input())
free_window = int(input())

cars = deque()
total_cars_passed = 0
crash_happened = False

while True:
    command = input()
    if command == "END":
        break

    if command == "green":
        current_green = green_light
        while cars and current_green > 0:
            car = cars.popleft()
            if len(car) <= current_green:
                current_green -= len(car)
                total_cars_passed += 1
            else:
                # Free window check
                remaining_length = len(car) - current_green
                if remaining_length <= free_window:
                    total_cars_passed += 1
                else:
                    print("A crash happened!")
                    print(f"{car} was hit at {car[current_green + free_window]}.")
                    crash_happened = True
                break
    else:
        cars.append(command)

if not crash_happened:
    print("Everyone is safe.")
    print(f"{total_cars_passed} total cars passed the crossroads.")
