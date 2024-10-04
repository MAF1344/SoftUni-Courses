n = int(input())

for i in range(n):
    text = input()
    is_pure = True
    for char in text:
        if char == ',' or char == '.' or char == '_':
            print(f"{text} is not pure!")
            is_pure = False
            break
    if is_pure:
        print(f"{text} is pure.")
