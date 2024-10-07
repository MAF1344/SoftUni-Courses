# Membaca input
cards = input().split()  # Baca daftar kartu dari input
shuffles = int(input())  # Baca jumlah shuffle yang diinginkan

# Mengulangi proses shuffle sebanyak jumlah yang diminta
for _ in range(shuffles):
    # Bagi deck menjadi dua bagian
    half = len(cards) // 2
    first_half = cards[:half]
    second_half = cards[half:]

    # Gabungkan dua bagian dengan cara menginterleave
    shuffled_deck = []
    for i in range(half):
        print(shuffled_deck)
        shuffled_deck.append(first_half[i])
        shuffled_deck.append(second_half[i])

    # Update deck dengan deck yang telah di-shuffle
    cards = shuffled_deck

# Cetak hasil akhir
print(cards)
