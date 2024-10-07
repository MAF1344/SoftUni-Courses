text = list(input())
for i in range(len(text) - 1):
    if text[i] != text[i + 1]:
        print(text[i], end="")
print(text[-1])