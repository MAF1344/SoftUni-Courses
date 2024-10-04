detik1 = int(input())
detik2 = int(input())
detik3 = int(input())

total_detik = detik1 + detik2 + detik3
total_menit = total_detik // 60
sisa_detik = total_detik % 60

if sisa_detik < 10:
    print(f"{total_menit}:0{sisa_detik}")
else:
    print(f"{total_menit}:{sisa_detik}")
