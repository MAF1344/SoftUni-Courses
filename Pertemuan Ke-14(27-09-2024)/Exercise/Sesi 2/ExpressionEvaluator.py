from collections import deque
expression = input().split()
numbers = deque()

for el in expression:
    if el.lstrip('-').isdigit():
        numbers.append(int(el))
    else:
        while len(numbers) > 1:
            first = numbers.popleft()
            second = numbers.popleft()
            if el == '+':
                result = first + second
            elif el == '-':
                result = first - second
            elif el == '*':
                result = first * second
            elif el == '/':
                result = first // second
            numbers.appendleft(result)

print(numbers[0])
