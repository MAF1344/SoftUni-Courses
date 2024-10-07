# Jumlah pompa bensin
N = int(input())

# List untuk menyimpan jumlah bensin dan jarak antar pompa
petrol_pump = []
for i in range(N):
    # Membaca jumlah bensin dan jarak, kemudian menyimpannya sebagai list dalam list
    petrol_pump.append(list(map(int, input().split())))

# Index pompa bensin awal, bensin saat ini, dan total bensin potensial
start = 0
current_petrol = 0
total_petrol = 0

# Iterasi melalui semua pompa bensin
for i in range(N):
    # Hitung perubahan bensin setelah mengisi dan menempuh jarak
    current_petrol += petrol_pump[i][0] - petrol_pump[i][1]
    total_petrol += petrol_pump[i][0] - petrol_pump[i][1]

    # Jika bensin saat ini kurang dari 0, berarti kita tidak bisa mencapai pompa berikutnya dari titik awal saat ini
    if current_petrol < 0:
        # Reset bensin saat ini dan ubah titik awal
        current_petrol = 0
        start = i + 1

# Jika total bensin potensial cukup, maka kita bisa menemukan titik awal yang valid
if total_petrol >= 0:
    print(start)
else:
    print("error")