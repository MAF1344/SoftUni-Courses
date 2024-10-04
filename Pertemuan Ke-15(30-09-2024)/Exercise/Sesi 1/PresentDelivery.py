def santa_present_delivery():
    m = int(input())  # Number of presents
    n = int(input())  # Size of the matrix
    neighborhood = []

    # Read the neighborhood matrix
    for _ in range(n):
        row = input().split()
        neighborhood.append(row)

    # Locate Santa's initial position
    santa_pos = None
    total_nice_kids = 0

    for r in range(n):
        for c in range(n):
            if neighborhood[r][c] == 'S':
                santa_pos = (r, c)
            if neighborhood[r][c] == 'V':
                total_nice_kids += 1

    # Define directions
    directions = {
        "up": (-1, 0),
        "down": (1, 0),
        "left": (0, -1),
        "right": (0, 1),
    }

    # Number of nice kids that have received presents
    delivered_presents = 0

    while m > 0:
        command = input().strip()

        if command == "Christmas morning":
            break

        if command in directions:
            dr, dc = directions[command]
            new_r = santa_pos[0] + dr
            new_c = santa_pos[1] + dc

            # Check if Santa moves within bounds
            if 0 <= new_r < n and 0 <= new_c < n:
                # Update Santa's current position to '-' before moving
                neighborhood[santa_pos[0]][santa_pos[1]] = "-"

                cell = neighborhood[new_r][new_c]

                if cell == "V":  # Nice kid
                    m -= 1  # Give a present
                    neighborhood[new_r][new_c] = "-"  # Mark as visited
                    delivered_presents += 1

                elif cell == "X":  # Naughty kid
                    neighborhood[new_r][new_c] = "-"  # Mark as visited, no present (in normal state)

                elif cell == "C":  # Cookies
                    neighborhood[new_r][new_c] = "-"
                    # Santa becomes generous and gives presents to kids around the cookie, including naughty kids
                    for adj_dr, adj_dc in directions.values():
                        adj_r = new_r + adj_dr
                        adj_c = new_c + adj_dc
                        if 0 <= adj_r < n and 0 <= adj_c < n:
                            # Both nice and naughty kids receive presents in this state
                            if neighborhood[adj_r][adj_c] == "V" and m > 0:
                                m -= 1
                                neighborhood[adj_r][adj_c] = "-"
                                delivered_presents += 1
                            elif neighborhood[adj_r][adj_c] == "X" and m > 0:
                                m -= 1
                                neighborhood[adj_r][adj_c] = "-"  # Naughty kid gets a present

                # Update Santa's new position
                santa_pos = (new_r, new_c)
                neighborhood[santa_pos[0]][santa_pos[1]] = "S"  # Mark new position of Santa as 'S'

        # If no presents left after the command
        if m <= 0:
            print("Santa ran out of presents!")
            break

    # Print the final state of the neighborhood
    for row in neighborhood:
        print(" ".join(row))

    # Final message regarding nice kids
    if delivered_presents == total_nice_kids:
        print(f"Good job, Santa! {delivered_presents} happy nice kid/s.")
    else:
        remaining_nice_kids = total_nice_kids - delivered_presents
        print(f"No presents for {remaining_nice_kids} nice kid/s.")

# Run the Santa delivery program
santa_present_delivery()
