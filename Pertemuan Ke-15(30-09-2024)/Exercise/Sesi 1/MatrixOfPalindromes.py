# Input jumlah baris (r) dan kolom (c)
rows, columns = map(int, input().split())

# Looping untuk menghasilkan matriks palindrome
for row in range(rows):
    for col in range(columns):
        # Huruf pertama dan terakhir ditentukan oleh baris
        first_last_letter = chr(97 + row)  # 'a' dimulai dari ASCII 97
        # Huruf tengah ditentukan oleh baris + kolom
        middle_letter = chr(97 + row + col)
        # Mencetak palindrome dalam format "first_last_middle_last"
        print(f"{first_last_letter}{middle_letter}{first_last_letter}", end=" ")
    print()  # Pindah ke baris berikutnya setelah selesai dengan satu baris kolom
