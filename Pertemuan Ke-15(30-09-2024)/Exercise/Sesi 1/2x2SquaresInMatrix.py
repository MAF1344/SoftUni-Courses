rows, columns = list(map(int, input().split()))
matrix = [[0] * columns for row in range(rows)]
equal_cells = 0

for x in range(rows):
    line = input().split()
    for y in range(columns):
        matrix[x][y] = line[y]

# Mengecek submatriks 2x2 yang semua elemennya sama
for x in range(rows - 1):  # Hindari iterasi baris terakhir
    for y in range(columns - 1):  # Hindari iterasi kolom terakhir
        # Cek apakah semua elemen dalam submatriks 2x2 sama
        if matrix[x][y] == matrix[x][y+1] == matrix[x+1][y] == matrix[x+1][y+1]:
            equal_cells += 1

print(equal_cells)
