def print_triangle(size):
    # Bagian atas segitiga (1 sampai size)
    for row in range(1, size + 1):
        for col in range(1, row + 1):
            print(col, end=" ")
        print()

    # Bagian bawah segitiga (size-1 sampai 1)
    for row in range(size - 1, 0, -1):
        for col in range(1, row + 1):
            print(col, end=" ")
        print()