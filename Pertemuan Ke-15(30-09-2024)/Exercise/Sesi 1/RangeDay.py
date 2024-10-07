def print_neighborhood(neighborhood):
    for row in neighborhood:
        print(" ".join(row))


def deliver_presents():
    m = int(input())
    n = int(input())

    neighborhood = [input().split() for _ in range(n)]
    commands = []

    santa_row, santa_col = 0, 0
    nice_kids = 0
    for r in range(n):
        for c in range(n):
            if neighborhood[r][c] == "S":
                santa_row, santa_col = r, c
            if neighborhood[r][c] == "V":
                nice_kids += 1

    directions = {
        "up": (-1, 0),
        "down": (1, 0),
        "left": (0, -1),
        "right": (0, 1)
    }

    def is_in_bounds(r, c):
        return 0 <= r < n and 0 <= c < n

    presents_delivered = 0

    def handle_cookies(r, c):
        nonlocal presents_delivered, m
        for direction in directions.values():
            nr, nc = r + direction[0], c + direction[1]
            if is_in_bounds(nr, nc) and neighborhood[nr][nc] in ["V", "X"]:
                if neighborhood[nr][nc] == "V":
                    presents_delivered += 1
                    m -= 1
                neighborhood[nr][nc] = "-"
                if m == 0:
                    break

    while True:
        command = input()
        if command == "Christmas morning":
            break

        direction = command
        move_r, move_c = directions[direction]
        new_row, new_col = santa_row + move_r, santa_col + move_c

        if is_in_bounds(new_row, new_col):
            neighborhood[santa_row][santa_col] = "-"  # Mark previous cell as empty
            santa_row, santa_col = new_row, new_col

            if neighborhood[santa_row][santa_col] == "V":
                presents_delivered += 1
                m -= 1
            elif neighborhood[santa_row][santa_col] == "C":
                handle_cookies(santa_row, santa_col)

            neighborhood[santa_row][santa_col] = "S"

        if m == 0:
            break

    remaining_nice_kids = sum(row.count("V") for row in neighborhood)

    if m == 0 and remaining_nice_kids > 0:
        print("Santa ran out of presents!")
    print_neighborhood(neighborhood)

    if remaining_nice_kids == 0:
        print(f"Good job, Santa! {presents_delivered} happy nice kid/s.")
    else:
        print(f"No presents for {remaining_nice_kids} nice kid/s.")

deliver_presents()