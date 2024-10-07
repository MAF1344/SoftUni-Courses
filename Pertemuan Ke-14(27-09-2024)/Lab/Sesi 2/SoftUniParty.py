guest = int(input())
guests = set()

while True:
    code = input()
    if code == "END":
        break
    if code in guests:
        guests.discard(code)
    else:
        guests.add(code)

print(len(guests))
for codes in sorted(guests):
    print(codes)