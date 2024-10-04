n = int(input())
matrix = []

# Memasukkan input ke dalam matriks
for rows in range(n):
    columns = list(map(int, input().split()))
    matrix.append(columns)

# Memproses perintah
while True:
    command = input()
    if command == "END":
        break
    tokens = command.split()
    row, col, value = int(tokens[1]), int(tokens[2]), int(tokens[3])

    # Pastikan indeks yang diberikan valid
    if 0 <= row < n and 0 <= col < len(matrix[row]):
        if tokens[0] == "Add":
            matrix[row][col] += value
        elif tokens[0] == "Subtract":  # Ejaan yang benar
            matrix[row][col] -= value
    else:
        print("Invalid coordinates")

# Mencetak matriks akhir
for row in matrix:
    print(*row)
