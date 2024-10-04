version_now = list(map(int, input().split('.')))
version_now[-1] += 1  # Tambahkan 1 ke angka versi terakhir

# Lakukan penyesuaian jika ada bagian yang lebih dari 9
for i in range(len(version_now) - 1, 0, -1):
    if version_now[i] > 9:
        version_now[i] = 0
        version_now[i - 1] += 1

# Jika digit pertama (major version) lebih dari 9, ini adalah aturan tambahan
if version_now[0] > 9:
    version_now[0] = 0

# Ubah kembali ke format string dengan tanda titik
version_update = '.'.join(map(str, version_now))

print(version_update)
