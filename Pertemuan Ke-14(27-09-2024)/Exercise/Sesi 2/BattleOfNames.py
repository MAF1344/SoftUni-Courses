n = int(input())
even_sum = set()
odd_sum = set()

for i in range(1, n + 1):  # Baris dimulai dari 1
    name = input()
    name_value = sum(ord(char) for char in name) // i  # Jumlah ASCII dibagi nomor baris
    if name_value % 2 == 0:
        even_sum.add(name_value)
    else:
        odd_sum.add(name_value)

# Hitung total sum dari setiap set
sum_even = sum(even_sum)
sum_odd = sum(odd_sum)

# Bandingkan dan lakukan operasi sesuai instruksi
if sum_even == sum_odd:
    result = odd_sum | even_sum  # Union
elif sum_odd > sum_even:
    result = odd_sum - even_sum  # Difference (Odd - Even)
else:
    result = odd_sum ^ even_sum  # Symmetric difference

# Cetak hasil, pisahkan dengan ", " dan urutkan
print(', '.join(map(str, result)))
