# Menerima input berupa string
input_string = input("Masukkan deretan angka yang dipisahkan oleh spasi: ")

# Mengonversi string input menjadi list angka
numbers = list(map(int, input_string.split()))

# Membuat list dengan angka yang sudah dibalik (positif menjadi negatif, negatif menjadi positif)
opposite_numbers = [-num for num in numbers]

# Mencetak hasil
print(opposite_numbers)
