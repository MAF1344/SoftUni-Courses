def easter_bunny():
    n = int(input())  # size of the field
    field = []
    bunny_pos = None

    # Read the field and find the bunny's position
    for i in range(n):
        row = input().split()
        if "B" in row:
            bunny_pos = (i, row.index("B"))
        field.append(row)

    # Directions: up, down, left, right
    directions = {
        "up": (-1, 0),
        "down": (1, 0),
        "left": (0, -1),
        "right": (0, 1),
    }

    max_eggs = 0
    best_direction = ""
    best_path = []

    # Helper function to collect eggs in a direction
    def collect_eggs(direction):
        eggs = 0
        path = []
        r, c = bunny_pos
        dr, dc = directions[direction]
        while True:
            r += dr
            c += dc
            if 0 <= r < n and 0 <= c < n and field[r][c] != "X":
                eggs += int(field[r][c])
                path.append([r, c])
            else:
                break
        return eggs, path

    # Check all directions
    for direction in directions:
        eggs, path = collect_eggs(direction)
        if eggs > max_eggs:
            max_eggs = eggs
            best_direction = direction
            best_path = path

    # Output the results
    print(best_direction)
    for step in best_path:
        print(step)
    print(max_eggs)


easter_bunny()
