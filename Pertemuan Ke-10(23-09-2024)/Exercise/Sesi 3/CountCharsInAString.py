text = input()
char_count = {}

for char in text:
    if char not in char_count:
        char_count[char] = 0
    char_count[char] += 1

for (key, value) in char_count.items():
    if key != " ":
        print(f"{key} -> {value}")