rows, columns = list(map(int, input().split()))
word = input()
matrix = []

# Panjang total dari snake
word_length = len(word)

for row in range(rows):
    words = []
    for col in range(columns):
        # Menghitung indeks karakter dari snake
        index = (row * columns + col) % word_length
        words.append(word[index])

    # Mengubah arah setiap baris ganjil
    if row % 2 == 1:
        words.reverse()

    matrix.append("".join(words))

# Cetak matriks
for line in matrix:
    print(line)
