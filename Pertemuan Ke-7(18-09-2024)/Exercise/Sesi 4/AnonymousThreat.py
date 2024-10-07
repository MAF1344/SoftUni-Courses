def anonymous_threat():
    data = input().split()
    commands = []
    while True:
        command = input()
        if command == "3:1":
            break
        commands.append(command)

    while commands:
        command = commands.pop(0).split()
        action = command[0]
        if action == "merge":
            start_idx = max(0, int(command[1]))
            end_idx = min(len(data) - 1, int(command[2]))
            merged = ''.join(data[start_idx:end_idx + 1])
            data = data[:start_idx] + [merged] + data[end_idx + 1:]
        elif action == "divide":
            idx = int(command[1])
            partitions = int(command[2])
            part_len = len(data[idx]) // partitions
            divided = [data[idx][i:i + part_len] for i in range(0, len(data[idx]), part_len)]
            data = data[:idx] + divided + data[idx + 1:]

    print(' '.join(data))

anonymous_threat()