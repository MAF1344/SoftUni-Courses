size = int(input())
matrix = [[0] * size for row in range(size)]

# Membuat matriks
for x in range(size):
    line = list(map(int, input().split(", ")))
    for y in range(size):
        matrix[x][y] = line[y]

# Mengambil angka-angka dari diagonal utama dan sekunder
primary_diagonal = []
secondary_diagonal = []

for i in range(size):
    primary_diagonal.append(matrix[i][i])
    secondary_diagonal.append(matrix[i][size - i - 1])

# Mencetak diagonal utama dan sekunder beserta jumlahnya
print(f"Primary diagonal: {', '.join(map(str, primary_diagonal))}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join(map(str, secondary_diagonal))}. Sum: {sum(secondary_diagonal)}")