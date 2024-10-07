N = int(input())

num = 1111
special_numbers = []

while num <= 9999:
    num_str = str(num)
    is_special = True

    for digit_char in num_str:
        digit = int(digit_char)
        if digit == 0 or N % digit != 0:
            is_special = False
            break

    if is_special:
        special_numbers.append(num)

    num += 1

print(' '.join(map(str, special_numbers)))