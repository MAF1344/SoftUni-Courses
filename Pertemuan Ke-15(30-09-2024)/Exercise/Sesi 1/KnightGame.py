# Fungsi untuk memeriksa apakah posisi berada dalam batas papan catur
def is_valid_move(n, row, col):
    return 0 <= row < n and 0 <= col < n

# Fungsi untuk menghitung jumlah knight yang dapat diserang oleh knight di posisi tertentu
def count_attacks(board, row, col, n):
    # Semua kemungkinan gerakan knight
    moves = [
        (-2, -1), (-2, 1), (2, -1), (2, 1),
        (-1, -2), (-1, 2), (1, -2), (1, 2)
    ]
    attacks = 0
    for move in moves:
        new_row, new_col = row + move[0], col + move[1]
        if is_valid_move(n, new_row, new_col) and board[new_row][new_col] == 'K':
            attacks += 1
    return attacks

# Membaca input
n = int(input())
board = [list(input()) for _ in range(n)]

removed_knights = 0

# Selama ada knight yang dapat menyerang, terus hapus knight dengan serangan terbanyak
while True:
    max_attacks = 0
    knight_pos = (-1, -1)

    # Cari knight dengan jumlah serangan terbesar
    for row in range(n):
        for col in range(n):
            if board[row][col] == 'K':
                attacks = count_attacks(board, row, col, n)
                if attacks > max_attacks:
                    max_attacks = attacks
                    knight_pos = (row, col)

    # Jika tidak ada knight yang bisa menyerang, berhenti
    if max_attacks == 0:
        break

    # Hapus knight yang bisa menyerang paling banyak
    board[knight_pos[0]][knight_pos[1]] = '0'
    removed_knights += 1

# Cetak jumlah knight yang dihapus
print(removed_knights)
