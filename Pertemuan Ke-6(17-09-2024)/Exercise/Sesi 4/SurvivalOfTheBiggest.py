numbers = input().split()
remove = int(input())

numbers = list(map(int, numbers))

for _ in range(remove):
    if numbers:
        min_value = min(numbers)
        numbers.remove(min_value)

numbers = list(map(str, numbers))

print(', '.join(numbers))