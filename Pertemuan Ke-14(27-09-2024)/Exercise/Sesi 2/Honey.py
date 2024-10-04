from collections import deque

def honey_production():
    # User input
    bees = list(map(int, input().split()))
    nectar = list(map(int, input().split()))
    operations = deque(input().split())

    bees = deque(bees)
    nectar = deque(nectar)
    total_honey = 0

    while bees and nectar:
        current_bee = bees.popleft()
        current_nectar = nectar.pop()

        if current_nectar >= current_bee:
            operation = operations.popleft()
            if operation == "+":
                total_honey += abs(current_bee + current_nectar)
            elif operation == "-":
                total_honey += abs(current_bee - current_nectar)
            elif operation == "*":
                total_honey += abs(current_bee * current_nectar)
            elif operation == "/":
                if current_nectar != 0:
                    total_honey += abs(current_bee // current_nectar)
        else:
            bees.appendleft(current_bee)

    print(f"Total honey made: {total_honey}")

    if bees:
        print(f"Bees left: {', '.join(map(str, bees))}")
    if nectar:
        print(f"Nectar left: {', '.join(map(str, nectar))}")

honey_production()