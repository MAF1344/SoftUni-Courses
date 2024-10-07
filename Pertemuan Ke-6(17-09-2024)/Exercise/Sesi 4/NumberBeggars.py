# Membaca input
numbers_str = input().strip()  # Membaca string dari input dan menghapus spasi ekstra
beggars_count = int(input().strip())  # Membaca jumlah beggars dan mengonversinya ke integer

# Mengonversi string angka menjadi list integer
numbers = list(map(int, numbers_str.split(', ')))

# Inisialisasi list untuk menyimpan total yang dikumpulkan oleh setiap beggar
beggars_sums = [0] * beggars_count

# Menghitung distribusi uang untuk setiap beggar
for i, number in enumerate(numbers):
    beggar_index = i % beggars_count  # Menentukan indeks beggar berdasarkan urutan
    print(beggar_index)
    beggars_sums[beggar_index] += number  # Menambahkan jumlah ke beggar yang sesuai

# Mencetak hasil
print(beggars_sums)
