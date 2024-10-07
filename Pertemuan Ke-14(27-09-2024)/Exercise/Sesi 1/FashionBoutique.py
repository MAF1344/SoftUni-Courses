clothes = list(map(int, input().split()))
rack_capacity = int(input())
racks = 0

n = 0
for weight in range(len(clothes)):
    n += clothes[weight]
    if n > rack_capacity:
        n = clothes[weight]
        racks += 1
if n > 0:
    racks += 1

print(racks)