text = input()

digits = ''.join([ch for ch in text if ch.isdigit()])
letters = ''.join([ch for ch in text if ch.isalpha()])
other = ''.join([ch for ch in text if not (ch.isdigit() or ch.isalpha())])

print(digits)
print(letters)
print(other)