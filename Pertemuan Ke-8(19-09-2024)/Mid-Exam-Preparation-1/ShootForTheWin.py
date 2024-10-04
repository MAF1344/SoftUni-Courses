targets = list(map(int, input().split()))

def shoot_for_the_win():
    while True:
        shoot = input()

        if shoot == 'End':
            break

        shoot = int(shoot)

        if shoot > len(targets) - 1 or targets[shoot] == -1:
            continue

        current_value = targets[shoot]
        targets[shoot] = -1

        for i in range(len(targets)):
            if targets[i] != -1:
                if targets[i] > current_value:
                    targets[i] -= current_value
                else:
                    targets[i] += current_value

    print(f"Shot targets: {targets.count(-1)} -> {' '.join(map(str, targets))}")

shoot_for_the_win()
