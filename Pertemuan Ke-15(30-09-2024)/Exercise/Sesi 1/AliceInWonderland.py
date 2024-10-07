# Input the size of the square matrix
n = int(input())

# Input the matrix (Wonderland territory)
wonderland = [input().split() for _ in range(n)]

# Find Alice's initial position
alice_pos = None
for i in range(n):
    if 'A' in wonderland[i]:
        alice_pos = (i, wonderland[i].index('A'))
        break

# Helper function to move Alice and check boundaries
def move_alice(direction, row, col):
    if direction == "up":
        return row - 1, col
    elif direction == "down":
        return row + 1, col
    elif direction == "left":
        return row, col - 1
    elif direction == "right":
        return row, col + 1

# Initialize variables
alice_row, alice_col = alice_pos
tea_collected = 0
is_game_over = False

# Mark Alice's starting position
wonderland[alice_row][alice_col] = '*'

# Process commands until Alice collects 10 tea bags or encounters the rabbit hole/out of bounds
while tea_collected < 10:
    command = input()

    # Move Alice
    alice_row, alice_col = move_alice(command, alice_row, alice_col)

    # Check if Alice goes out of bounds
    if not (0 <= alice_row < n and 0 <= alice_col < n):
        is_game_over = True
        break

    # Check the current cell where Alice moved
    current_cell = wonderland[alice_row][alice_col]

    if current_cell == "R":
        # Alice fell into the rabbit hole
        is_game_over = True
        wonderland[alice_row][alice_col] = '*'  # Mark her final position
        break
    elif current_cell.isdigit():
        # Alice collects tea bags
        tea_collected += int(current_cell)

    # Mark the path Alice walked
    wonderland[alice_row][alice_col] = '*'

# Output results
if is_game_over:
    print("Alice didn't make it to the tea party.")
else:
    print("She did it! She went to the party.")

# Ensure rabbit hole position is correctly marked with '*'
for row in wonderland:
    print(' '.join(row))