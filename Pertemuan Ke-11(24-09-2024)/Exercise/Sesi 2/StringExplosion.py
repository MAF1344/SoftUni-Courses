text = input()
explosion_strength = 0
result = []
for i in range(len(text)):
    if text[i] == '>':
        result.append(text[i])
        explosion_strength += int(text[i + 1])
    elif explosion_strength > 0:
        explosion_strength -= 1
    else:
        result.append(text[i])
print("".join(result))