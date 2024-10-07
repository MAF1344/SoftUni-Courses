def escape_maze():
    # Get the size of the matrix
    n = int(input())

    # Read the matrix row by row
    matrix = [list(input()) for _ in range(n)]

    # Locate the player starting position
    health = 100
    position = [0, 0]

    for i in range(n):
        if 'P' in matrix[i]:
            position = [i, matrix[i].index('P')]
            break

    # Read the commands (directions)
    commands = []
    while True:
        try:
            command = input()
            if command:
                commands.append(command)
            else:
                break
        except EOFError:
            break

    # Execute each command
    for command in commands:
        # Calculate new position based on command
        new_pos = position.copy()

        if command == 'up':
            new_pos[0] -= 1
        elif command == 'down':
            new_pos[0] += 1
        elif command == 'left':
            new_pos[1] -= 1
        elif command == 'right':
            new_pos[1] += 1

        # Check if new position is inside maze boundaries
        if 0 <= new_pos[0] < n and 0 <= new_pos[1] < n:
            # Mark the old position as empty
            matrix[position[0]][position[1]] = '-'

            pos_value = matrix[new_pos[0]][new_pos[1]]

            if pos_value == 'M':  # Monster encountered
                health -= 40
                if health <= 0:
                    matrix[new_pos[0]][new_pos[1]] = 'P'  # Mark player's last position
                    print("Player is dead. Maze over!")
                    print(f"Player's health: 0 units")
                    for row in matrix:
                        print(''.join(row))
                    return
                else:
                    matrix[new_pos[0]][new_pos[1]] = '-'  # Remove the monster

            elif pos_value == 'H':  # Health potion encountered
                health = min(100, health + 15)
                matrix[new_pos[0]][new_pos[1]] = '-'  # Remove health potion

            elif pos_value == 'X':  # Exit found
                matrix[new_pos[0]][new_pos[1]] = 'P'  # Mark the exit with player
                print("Player escaped the maze. Danger passed!")
                print(f"Player's health: {health} units")
                for row in matrix:
                    print(''.join(row))
                return

            # Move the player to the new position
            position = new_pos

    # If all commands are processed and player did not exit the maze or die
    matrix[position[0]][position[1]] = 'P'
    print(f"Player's health: {health} units")
    for row in matrix:
        print(''.join(row))


# Run the function to test the input
escape_maze()
