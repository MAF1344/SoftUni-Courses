first_sequence = set(map(int, input().split()))
second_sequence = set(map(int, input().split()))
n = int(input())

for _ in range(n):
    command = input().split()
    if command[0] == "Add":
        numbers = set(map(int, command[2:]))
        if command[1] == "First":
            first_sequence.update(numbers)
        elif command[1] == "Second":
            second_sequence.update(numbers)
    elif command[0] == "Remove":
        numbers = set(map(int, command[2:]))
        if command[1] == "First":
            first_sequence.difference_update(numbers)
        elif command[1] == "Second":
            second_sequence.difference_update(numbers)
    elif command[0] == "Check" and command[1] == "Subset":
        print(first_sequence.issubset(second_sequence) or second_sequence.issubset(first_sequence))

print(", ".join(map(str, sorted(first_sequence))))
print(", ".join(map(str, sorted(second_sequence))))
