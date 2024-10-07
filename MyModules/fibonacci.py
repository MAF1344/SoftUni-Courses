def fibonacci_sequence(commands):
    numbers = []

    for command in commands:
        tokens = command.split()

        if not tokens:  # Menangani input kosong
            continue

        if tokens[0] == "Create" and len(tokens) > 2 and tokens[1] == "Sequence":
            count = int(tokens[2])
            sequence = create_fibonacci(count)
            numbers.extend(sequence)
            print(" ".join(map(str, sequence)))

        elif tokens[0] == "Locate" and len(tokens) > 1:
            number_to_locate = int(tokens[1])
            locate_number(numbers, number_to_locate)


def create_fibonacci(count):
    if count <= 0:
        return []
    sequence = [0, 1]
    for i in range(2, count):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence[:count]


def locate_number(numbers, number):
    if number in numbers:
        index = numbers.index(number)
        print(f"The number - {number} is at index {index}")
    else:
        print(f"The number {number} is not in the sequence")


# Input dari user
if __name__ == "__main__":
    commands = []
    while True:
        command = input()
        if command == "Stop":
            break
        commands.append(command)

    fibonacci_sequence(commands)
