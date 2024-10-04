n = int(input())
periodic_table = set()

for num in range(n):
    elements = input().split()
    for element in elements:
        periodic_table.add(element)

print('\n'.join(sorted(periodic_table)))