size = int(input())
matrix = [[0] * size for row in range(size)]

for x in range(size):
    line = list(map(int, input().split()))
    for y in range(size):
        matrix[x][y] = line[y]

primary_diagonal = []
secondary_diagonal = []

for i in range(size):
    primary_diagonal.append(matrix[i][i])
    secondary_diagonal.append(matrix[i][size - i - 1])

if sum(primary_diagonal) > sum(secondary_diagonal):
    print(sum(primary_diagonal) - sum(secondary_diagonal))
else:
    print(sum(secondary_diagonal) - sum(primary_diagonal))