import sys

put = input()
min = sys.maxsize

while put != "Stop":
    num = int(put)

    if num < min:
        min = num
    put = input()

print(min)