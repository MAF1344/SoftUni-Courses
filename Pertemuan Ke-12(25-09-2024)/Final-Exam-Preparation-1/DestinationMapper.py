import re

place = input()

# Regex untuk mencocokkan lokasi yang valid: diapit oleh karakter yang sama (= atau /) dan memiliki setidaknya 3 huruf
pattern = r"([=/])([A-Z][a-zA-Z]{2,})\1"
matches = re.finditer(pattern, place)

# Mengambil kata-kata yang valid dari hasil pencocokan regex
filtered_words = [match.group(2) for match in matches]

# Menghitung total travel points berdasarkan panjang semua kata yang valid
travel_points = sum(len(word) for word in filtered_words)

# Mencetak hasil sesuai format
if filtered_words:
    print(f"Destinations: {', '.join(filtered_words)}")
else:
    print("Destinations:")

print(f"Travel Points: {travel_points}")
