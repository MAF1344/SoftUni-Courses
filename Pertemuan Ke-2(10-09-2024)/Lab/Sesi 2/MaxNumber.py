import sys

put = input()
max = -sys.maxsize

while put != "Stop":
    num = int(put)

    if num > max:
        max = num
    put = input()

print(max)