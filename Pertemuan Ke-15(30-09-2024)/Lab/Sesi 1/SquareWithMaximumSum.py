# Membaca ukuran matriks
rows, cols = map(int, input().split(", "))

matrix = []

# Membaca elemen matriks
for _ in range(rows):
    line = [int(x) for x in input().split(", ")]
    matrix.append(line)

# Inisialisasi variabel untuk menyimpan submatriks dengan jumlah terbesar
max_sum = float('-inf')
top_left_submatrix = []

# Mencari submatriks 2x2 dengan jumlah terbesar
for i in range(rows - 1):  # -1 untuk menghindari IndexError
    for j in range(cols - 1):  # -1 untuk menghindari IndexError
        current_sum = (
                matrix[i][j] + matrix[i][j + 1] +
                matrix[i + 1][j] + matrix[i + 1][j + 1]
        )

        if current_sum > max_sum:
            max_sum = current_sum
            top_left_submatrix = [
                [matrix[i][j], matrix[i][j + 1]],
                [matrix[i + 1][j], matrix[i + 1][j + 1]]
            ]

# Mencetak submatriks dan jumlah elemen
for row in top_left_submatrix:
    print(" ".join(map(str, row)))

print(max_sum)