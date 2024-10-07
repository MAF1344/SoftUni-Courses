import re

banned_words = input().split(", ")
text = input()

for word in banned_words:
    # Menggunakan regex untuk mengganti seluruh kata yang disensor
    text = re.sub(r'\b' + re.escape(word) + r'\b', '*' * len(word), text)

print(text)