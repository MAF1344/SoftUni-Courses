strings = input().split('|')  # Pisahkan input berdasarkan '|'
num_strings = []

# Balik setiap bagian dan tambahkan ke daftar num_strings
for part in reversed(strings):
    num_strings.extend(part.split())  # Pisahkan angka-angka dalam setiap bagian dan tambahkan ke num_strings

print(' '.join(num_strings))  # Cetak hasil sebagai string yang dipisahkan spasi