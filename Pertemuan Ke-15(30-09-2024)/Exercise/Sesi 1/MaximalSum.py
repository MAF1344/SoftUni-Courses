rows, columns = list(map(int, input().split()))
matrix = [[0] * columns for row in range(rows)]
max_sum_matrix = float('-inf')  # Memulai dengan nilai paling kecil
new_matrix = []

# Mengisi matriks
for x in range(rows):
    line = list(map(int, input().split()))
    for y in range(columns):
        matrix[x][y] = line[y]

# Mengecek submatriks 3x3 dengan jumlah elemen terbesar
for x in range(rows - 2):  # Hindari iterasi baris terakhir yang tidak bisa membentuk 3x3
    for y in range(columns - 2):  # Hindari iterasi kolom terakhir
        current_sum = (
            matrix[x][y] + matrix[x][y+1] + matrix[x][y+2] +
            matrix[x+1][y] + matrix[x+1][y+1] + matrix[x+1][y+2] +
            matrix[x+2][y] + matrix[x+2][y+1] + matrix[x+2][y+2]
        )

        # Jika current_sum lebih besar dari max_sum_matrix, perbarui max_sum_matrix dan new_matrix
        if current_sum > max_sum_matrix:
            max_sum_matrix = current_sum
            new_matrix = [
                [matrix[x][y], matrix[x][y+1], matrix[x][y+2]],
                [matrix[x+1][y], matrix[x+1][y+1], matrix[x+1][y+2]],
                [matrix[x+2][y], matrix[x+2][y+1], matrix[x+2][y+2]]
            ]

# Output nilai maksimum dan submatriks
print(f"Sum = {max_sum_matrix}")
for row in new_matrix:
    print(' '.join(map(str, row)))