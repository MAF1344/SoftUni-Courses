def pokemon_dont_go():
    distances = list(map(int, input().split()))
    total_sum = 0

    while distances:
        index = int(input())

        if index < 0:
            # Index kurang dari 0: ambil elemen pertama, ganti dengan elemen terakhir
            removed_value = distances[0]
            distances[0] = distances[-1]
        elif index >= len(distances):
            # Index lebih besar dari panjang array: ambil elemen terakhir, ganti dengan elemen pertama
            removed_value = distances[-1]
            distances[-1] = distances[0]
        else:
            # Ambil elemen di index yang valid
            removed_value = distances.pop(index)

        total_sum += removed_value

        # Ubah jarak setelah menghapus elemen
        distances = [x + removed_value if x <= removed_value else x - removed_value for x in distances]

    print(total_sum)

# Example usage:
pokemon_dont_go()