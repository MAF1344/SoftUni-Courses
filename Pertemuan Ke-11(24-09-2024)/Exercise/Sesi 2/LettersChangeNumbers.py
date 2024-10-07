import string

def get_position(letter):
    if letter.islower():
        return ord(letter) - ord('a') + 1
    else:
        return ord(letter) - ord('A') + 1

strings = input().split()
total_sum = 0

for s in strings:
    first_letter = s[0]
    last_letter = s[-1]
    number = int(s[1:-1])

    if first_letter.isupper():
        total_sum += number / get_position(first_letter)
    else:
        total_sum += number * get_position(first_letter)

    if last_letter.isupper():
        total_sum -= get_position(last_letter)
    else:
        total_sum += get_position(last_letter)

print(f"{total_sum:.2f}")