# Membaca ukuran matriks
N = int(input())

# Membaca matriks
matrix = []
for _ in range(N):
    row = list(map(int, input().split()))
    matrix.append(row)

# Membaca koordinat bom
bombs_input = input().split()
bombs = []
for bomb in bombs_input:
    row, col = map(int, bomb.split(','))
    bombs.append((row, col))

# Daftar arah untuk ledakan bom (8 arah)
directions = [(-1, -1), (-1, 0), (-1, 1),
              (0, -1),         (0, 1),
              (1, -1), (1, 0), (1, 1)]

# Memproses setiap bom
for row, col in bombs:
    bomb_value = matrix[row][col]  # Mendapatkan nilai bom
    matrix[row][col] = 0  # Mengatur nilai bom menjadi 0

    # Menerapkan kerusakan pada sel-sel di sekitar bom
    for dr, dc in directions:
        r, c = row + dr, col + dc
        if 0 <= r < N and 0 <= c < N:  # Pastikan dalam batas matriks
            if matrix[r][c] > 0:  # Hanya mengurangi nilai jika sel masih hidup
                matrix[r][c] -= bomb_value

# Menghitung sel yang masih hidup dan jumlah nilai mereka
alive_cells = 0
sum_of_cells = 0

for r in range(N):
    for c in range(N):
        if matrix[r][c] > 0:
            alive_cells += 1
            sum_of_cells += matrix[r][c]

# Mencetak hasil
print(f"Alive cells: {alive_cells}")
print(f"Sum: {sum_of_cells}")

# Mencetak matriks
for row in matrix:
    print(' '.join(map(str, row)))
