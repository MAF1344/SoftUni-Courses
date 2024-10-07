first_code = int(input())
second_code = int(input())

first_code = str(first_code)
second_code = str(second_code)

if len(first_code) != 4 or len(second_code) != 4:
    print("Error")
else:
    for d1 in range(int(first_code[0]), int(second_code[0]) + 1):
        for d2 in range(int(first_code[1]), int(second_code[1]) + 1):
            for d3 in range(int(first_code[2]), int(second_code[2]) + 1):
                for d4 in range(int(first_code[3]), int(second_code[3]) + 1):
                    if d1 % 2 != 0 and d2 % 2 != 0 and d3 % 2 != 0 and d4 % 2 != 0:
                        print(f"{d1}{d2}{d3}{d4}", end=" ")