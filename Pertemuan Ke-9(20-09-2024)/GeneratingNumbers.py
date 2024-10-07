def generate_numbers():
    numbers = list(map(int, input().split()))

    while True:
        command = input().strip()

        if command == "END":
            break

        if command.startswith("add to start"):
            new_numbers = list(map(int, command.split()[3:]))
            numbers = new_numbers + numbers

        elif command.startswith("remove greater than"):
            value = int(command.split()[3])
            numbers = [num for num in numbers if num <= value]

        elif command.startswith("replace"):
            _, _, value, replacement = command.split()
            value = int(value)
            replacement = int(replacement)
            if value in numbers:
                index = numbers.index(value)
                numbers[index] = replacement

        elif command.startswith("remove at index"):
            index = int(command.split()[3])
            if 0 <= index < len(numbers):
                numbers.pop(index)

        elif command == "find even":
            evens = [num for num in numbers if num % 2 == 0]
            print(" ".join(map(str, evens)))

        elif command == "find odd":
            odds = [num for num in numbers if num % 2 != 0]
            print(" ".join(map(str, odds)))

    print(", ".join(map(str, numbers)))

generate_numbers()