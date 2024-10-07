n = int(input())
money = 100

# Create a board (n x n)
boards = []
for rows in range(n):
    board = []
    for column in range(n):
        board.append("-")
    boards.append(board)

# Replace the contents of the board with input from the user
for i in range(n):
    area = list(input())  # Take input for each row
    for j in range(n):
        boards[i][j] = area[j]  # Update the board using row index i and column index j

# Find initial position of gambler (G)
row, col = next(((i, j) for i in range(n) for j in range(n) if boards[i][j] == 'G'), (None, None))

# Directions that can be received
directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

while money > 0:
    # Receive command/direction
    command = input()
    if command == "end":
        break

    if command not in directions:
        print("Invalid command!")
        continue

    # Calculate new position
    d_row, d_col = directions[command]
    new_row, new_col = row + d_row, col + d_col

    # Check if new position is within bounds
    if 0 <= new_row < n and 0 <= new_col < n:
        # Update the position of the gambler in the board
        boards[row][col] = '-'  # Change the previous position to "-"
        row, col = new_row, new_col  # Update gambler position

        if boards[row][col] == 'W':
            money += 100

        elif boards[row][col] == 'P':
            money -= 200

        elif boards[row][col] == 'J':
            money += 100000
            print("You win the Jackpot!")
            break

        # Mark the new position of the gambler
        boards[row][col] = 'G'

    else:
        print("You went out of bounds!")
        money = 0  # Set money to 0 to trigger the game over condition
        break

    # Check if money is zero or less after the move
    if money <= 0:
        break

if money <= 0:
    # if gambler lost games
    print("Game over! You lost everything!")
else:
    # final amount of gambler
    print(f"End of the game. Total amount: {money}$")
    # Print the final board (final position of gambler in the board)
    for row in boards:
        print("".join(row))  # Join each row list into a string for easier visualization
