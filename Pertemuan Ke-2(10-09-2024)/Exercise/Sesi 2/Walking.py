steps = 0

while True:
    step = input()

    if step == 'Going home':
        last_steps = int(input())
        steps += last_steps
        break

    steps += int(step)

    if steps >= 10000:
        break

if steps >= 10000:
    print("Goal reached! Good job!")
    print(f"{steps - 10000} steps over the goal!")
else:
    print(f"{10000 - steps} more steps to reach goal.")
