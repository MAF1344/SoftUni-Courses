long = int(input())
wide = int(input())
pieces = long * wide
taken = 0

while True:
    take = input()
    if take == 'STOP':
        break

    take = int(take)
    pieces -= take
    taken += take

    if pieces <= 0:
        break

if pieces >= 0:
    print(f"{pieces} pieces are left.")
else:
    print(f"No more cake left! You need {abs(pieces)} pieces more.")