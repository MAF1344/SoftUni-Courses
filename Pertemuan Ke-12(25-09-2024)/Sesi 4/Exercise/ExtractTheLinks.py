import re

# Pola regex untuk menangkap tautan yang valid
link_pattern = r'www\.[A-Za-z0-9-]+(\.[a-z]+)+'

while True:
    line = input()
    if not line:
        break
    # Temukan semua kecocokan menggunakan finditer
    matches = re.finditer(link_pattern, line)
    for match in matches:
        # Cetak seluruh kecocokan
        print(match.group())
