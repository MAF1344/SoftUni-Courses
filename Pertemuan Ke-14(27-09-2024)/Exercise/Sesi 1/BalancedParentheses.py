parentheses = input()
stack = []
is_balanced = True

for char in parentheses:
    if char in ['(', '{', '[']:
        stack.append(char)
    elif char in [')', '}', ']']:
        if not stack:  # Jika stack kosong saat menemukan tanda kurung tutup
            is_balanced = False
            break
        top = stack.pop()  # Ambil elemen teratas stack
        if (char == ')' and top != '(') or (char == '}' and top != '{') or (char == ']' and top != '['):
            is_balanced = False
            break

if is_balanced and not stack:  # Jika stack kosong dan seimbang
    print("YES")
else:
    print("NO")