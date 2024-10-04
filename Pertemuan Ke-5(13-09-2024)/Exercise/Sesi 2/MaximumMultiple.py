divisor = int(input())
boundary = int(input())

total_divisor = 0

while True:
    total_divisor += divisor
    if total_divisor > boundary:
        total_divisor -= divisor
        break

print(total_divisor)