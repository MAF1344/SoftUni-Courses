from collections import deque

queue = deque()
water_quantity = int(input())

# Menerima nama sampai "Start"
while True:
    name = input()
    if name == "Start":
        break
    queue.append(name)

# Menerima perintah sampai "End"
command = input()
while command != "End":
    if "refill" in command:
        # Memisahkan perintah dan mengambil jumlah liter yang diisi ulang
        _, amount = command.split()  # Memisahkan perintah 'refill' dan angka
        water_quantity += int(amount)  # Menambahkan jumlah liter ke total air
    else:
        liters = int(command)  # Mendapatkan jumlah liter yang diminta
        if liters <= water_quantity:
            water_quantity -= liters
            print(f"{queue.popleft()} got water")
        else:
            print(f'{queue.popleft()} must wait')
    command = input()

# Menampilkan jumlah air yang tersisa
print(f"{water_quantity} liters left")