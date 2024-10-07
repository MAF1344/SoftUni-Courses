text = input()
for char in text:
    char = ord(char) + 3
    print(chr(char), end="")