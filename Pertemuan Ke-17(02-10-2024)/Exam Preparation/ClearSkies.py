n = int(input())
armor = 300

# Create a matrix (n x n)
matriks = []
for rows in range(n):
    matrix = []
    for column in range(n):
        matrix.append("-")
    matriks.append(matrix)

# Replace the contents of the matrix with input from the user
for i in range(n):
    area = list(input())  # Take input for each row
    for j in range(n):
        matriks[i][j] = area[j]  # Update the matrix using row index i and column index j

# Find initial position of jet (J)
row, col = next(((i, j) for i in range(n) for j in range(n) if matriks[i][j] == 'J'), (None, None))

# Directions that can be received
directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

while armor > 0:
    # Receive command/direction
    command = input()
    if command not in directions:
        print("Invalid command!")
        continue

    # Calculate new position
    d_row, d_col = directions[command]
    new_row, new_col = row + d_row, col + d_col

    # Check if new position is within bounds
    if 0 <= new_row < n and 0 <= new_col < n:
        # Update the position of the jet in the matrix
        matriks[row][col] = '-'  # Change the previous position to "-"
        row, col = new_row, new_col  # Update jet position

        if matriks[row][col] == 'R':
            armor = 300

        # Check if jet encounters an enemy
        if matriks[row][col] == 'E':
            # Check if this is the last enemy
            if sum(row.count('E') for row in matriks) == 1:
                matriks[row][col] = 'J'  # Neutralize the last enemy
                print(f"Mission accomplished, you neutralized the aerial threat!")
                break
            else:
                armor -= 100  # Reduce armor points
                matriks[row][col] = '-'  # Neutralize the enemy

        # Mark the new position of the jet
        matriks[row][col] = 'J'

    else:
        print("Out of bounds! Please enter a valid command.")

if armor <= 0:
    # Display last position of the jet
    print(f"Mission failed, your jetfighter was shot down! Last coordinates [{row}, {col}]!")

# Print the final matrix (final position of jet in the matrix)
for row in matriks:
    print("".join(row))  # Join each row list into a string for easier visualization
