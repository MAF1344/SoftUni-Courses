from collections import deque

queue = deque(input().split())  # Memasukkan daftar nama ke dalam queue
toss = int(input())  # Jumlah hitungan

while len(queue) > 1:
    # Hitung sampai `toss`, pindahkan nama ke belakang sampai hitungan selesai
    queue.rotate(-(toss - 1))  # Memindahkan elemen ke kiri sebanyak toss - 1
    print(f"Removed {queue.popleft()}")  # Keluarkan elemen terdepan yang kena hitungan

# Saat tersisa satu anak
print(f"Last is {queue[0]}")