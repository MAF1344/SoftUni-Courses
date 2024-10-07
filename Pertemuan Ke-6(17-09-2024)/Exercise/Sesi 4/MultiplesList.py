multiple = int(input())
factor = int(input())
list = []

for i in range(multiple, factor * multiple + 1, multiple):
    list.append(i)

print(list)