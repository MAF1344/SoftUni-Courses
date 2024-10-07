def array_modifier():
    arr = list(map(int, input().split()))

    while True:
        command = input().split()

        if command[0] == "end":
            print(", ".join(map(str, arr)))
            break
        elif command[0] == "swap":
            index1, index2 = int(command[1]), int(command[2])
            arr[index1], arr[index2] = arr[index2], arr[index1]
        elif command[0] == "multiply":
            index1, index2 = int(command[1]), int(command[2])
            arr[index1] *= arr[index2]
        elif command[0] == "decrease":
            arr = [x - 1 for x in arr]

array_modifier()