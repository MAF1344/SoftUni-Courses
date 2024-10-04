# Menerima input dari pengguna
str1, str2 = input().split()

# Inisialisasi variabel total_sum
total_sum = 0

# Iterasi dengan panjang minimum dari kedua string
for i in range(min(len(str1), len(str2))):
    total_sum += ord(str1[i]) * ord(str2[i])

# Jika str1 lebih panjang, tambahkan sisa karakter dari str1
for i in range(min(len(str1), len(str2)), len(str1)):
    total_sum += ord(str1[i])

# Jika str2 lebih panjang, tambahkan sisa karakter dari str2
for i in range(min(len(str1), len(str2)), len(str2)):
    total_sum += ord(str2[i])

# Cetak hasil total
print(total_sum)
