# Meminta input dari pengguna
num = input()

# Memecah input berdasarkan ', ' dan mengonversi menjadi list of strings
numbers = num.split(', ')

# Fungsi untuk mengecek apakah angka adalah palindrom
def is_palindrome(number):
    # Mengonversi angka ke string dan membandingkan dengan kebalikannya
    return str(number) == str(number)[::-1]

# Mengecek setiap angka apakah palindrom atau tidak
for n in numbers:
    if is_palindrome(n):  # Memanggil fungsi is_palindrome untuk setiap angka
        print(True)
    else:
        print(False)
