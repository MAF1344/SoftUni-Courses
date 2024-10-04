electrons = int(input())

shells = []
n = 1

while electrons > 0:
    electron_lost = 2 * (n ** 2)
    if electrons < electron_lost:
        shells.append(electrons)
        electrons = 0
    else:
        shells.append(electron_lost)
        electrons -= electron_lost
    n += 1

print(shells)