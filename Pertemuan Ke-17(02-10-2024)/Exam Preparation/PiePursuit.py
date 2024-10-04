from collections import deque

contestants = [int(x) for x in input().split()]
pies = deque(int(x) for x in input().split())

while contestants and pies:
    contestant = contestants.pop()
    pie = pies.popleft()

    difference = abs(contestant - pie)

    if contestant >= pie:
        if difference > 0:
            contestants.append(difference)
        continue

    if len(pies) == 0:
        pies.append(difference)
        continue

    if difference == 1:
        pies[0] += difference
        continue

    pies.appendleft(difference)

if not pies and contestants:
    print('We will have to wait for more pies to be baked!')
    print(f'Contestants left: {", ".join(str(x) for x in contestants)}')

elif not pies and not contestants:
    print('We have a champion!')

elif pies and not contestants:
    print('Our contestants need to rest!')
    print(f'Pies left: {", ".join(str(x) for x in pies)}')