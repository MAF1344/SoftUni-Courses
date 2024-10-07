floors = int(input())
rooms = int(input())

for i in range(floors, 0, -1):
    if i % 2 == 0:
        prefix = "O"
    else:
        prefix = "A"

    for j in range(rooms):
        if i == floors:
            print(f"L{i}{j} ", end="")
        else:
            print(f"{prefix}{i}{j} ", end="")
    print("")