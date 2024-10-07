quantity = int(input())
orders = list(map(int, input().split()))
print(max(orders))

orders_left = []
orders_rejected = False

for order in orders:
    if quantity >= order:
        quantity -= order
    else:
        orders_left.append(order)
        orders_rejected = True  # Flag untuk menandakan bahwa pesanan ditolak
        break  # Hentikan loop saat pesanan pertama kali ditolak

# Tambahkan semua pesanan berikutnya setelah pesanan pertama yang ditolak
if orders_rejected:
    orders_left.extend(orders[orders.index(order)+1:])

# Jika tidak ada pesanan yang tersisa di `orders_left`, berarti semua pesanan telah diproses
if not orders_left:
    print("Orders complete")
else:
    print(f"Orders left: {' '.join(map(str, orders_left))}")
