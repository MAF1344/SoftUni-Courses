num = int(input())
stack = []

for _ in range(num):
    command = input().split()
    operation = int(command[0])

    if operation == 1:
        value = int(command[1])
        stack.append(value)
    elif operation == 2 and stack:
        stack.pop()
    elif operation == 3 and stack:
        print(max(stack))
    elif operation == 4 and stack:
        print(min(stack))
    else:
        continue

print(', '.join(map(str, reversed(stack))))