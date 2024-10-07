import re

# Pola regex untuk email yang valid
email_pattern = r'(?<![-._])\b[A-Za-z0-9]+[A-Za-z0-9._-]*@[A-Za-z-]+(\.[A-Za-z]+)+\b'

# Input dari pengguna
text = input()

# Temukan semua kecocokan menggunakan finditer agar seluruh email ditemukan
matches = re.finditer(email_pattern, text)

# Ambil setiap kecocokan dan cetak hasilnya
for match in matches:
    print(match.group())
