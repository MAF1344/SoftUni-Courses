def spread_bunnies(lair, rows, cols):
    """Function to spread bunnies one step in all directions"""
    new_bunnies = set()
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

    for r in range(rows):
        for c in range(cols):
            if lair[r][c] == 'B':
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols:
                        new_bunnies.add((nr, nc))

    for r, c in new_bunnies:
        lair[r][c] = 'B'


def move_player(lair, player_pos, move):
    """Function to move player"""
    moves = {'L': (0, -1), 'R': (0, 1), 'U': (-1, 0), 'D': (1, 0)}
    pr, pc = player_pos
    dr, dc = moves[move]
    new_r, new_c = pr + dr, pc + dc

    # If player goes out of bounds
    if not (0 <= new_r < len(lair) and 0 <= new_c < len(lair[0])):
        lair[pr][pc] = '.'  # Clear the previous player position
        return 'won', pr, pc

    # If player moves to a bunny cell
    if lair[new_r][new_c] == 'B':
        lair[pr][pc] = '.'  # Clear the previous player position
        return 'dead', new_r, new_c

    # Move player to the new cell
    lair[pr][pc] = '.'  # Clear the previous player position
    lair[new_r][new_c] = 'P'
    return 'move', new_r, new_c


def play_game(lair, directions):
    """Main function to simulate the game"""
    rows, cols = len(lair), len(lair[0])
    player_pos = None

    # Find initial position of the player
    for r in range(rows):
        for c in range(cols):
            if lair[r][c] == 'P':
                player_pos = (r, c)
                break
        if player_pos:
            break

    for move in directions:
        status, new_r, new_c = move_player(lair, player_pos, move)
        if status != 'move':
            spread_bunnies(lair, rows, cols)
            for row in lair:
                print(''.join(row))
            print(f"{status}: {new_r} {new_c}")
            return

        # Update player position
        player_pos = (new_r, new_c)

        # Spread bunnies after each move
        spread_bunnies(lair, rows, cols)

        # Check if bunnies have reached the player after spreading
        if lair[new_r][new_c] == 'B':
            for row in lair:
                print(''.join(row))
            print(f"dead: {new_r} {new_c}")
            return

    # If player has survived all moves
    for row in lair:
        print(''.join(row))
    print(f"won: {new_r} {new_c}")


# Input handling
N, M = map(int, input().split())
lair = [list(input().strip()) for _ in range(N)]
directions = input().strip()

# Play the game
play_game(lair, directions)
