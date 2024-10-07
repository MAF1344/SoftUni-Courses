# Input field size
field_size = int(input())

# Input commands for the miner's movement
commands = input().split()

# Initialize the field
field = [input().split() for _ in range(field_size)]

# Find the initial position of the miner
miner_position = None
total_coal = 0

for row in range(field_size):
    for col in range(field_size):
        if field[row][col] == 's':
            miner_position = (row, col)
        elif field[row][col] == 'c':
            total_coal += 1

# Directions dictionary for movement
directions = {
    "left": (0, -1),
    "right": (0, 1),
    "up": (-1, 0),
    "down": (1, 0)
}

# Collecting coal counter
collected_coal = 0


# Function to check if the position is within the bounds
def in_bounds(row, col):
    return 0 <= row < field_size and 0 <= col < field_size


# Processing each command
for command in commands:
    if command in directions:
        # Get the new position
        delta_row, delta_col = directions[command]
        new_row = miner_position[0] + delta_row
        new_col = miner_position[1] + delta_col

        if in_bounds(new_row, new_col):
            miner_position = (new_row, new_col)
            current_cell = field[new_row][new_col]

            if current_cell == 'c':  # Found coal
                collected_coal += 1
                field[new_row][new_col] = '*'  # Replace coal with '*'

                if collected_coal == total_coal:  # Collected all coal
                    print(f"You collected all coal! ({new_row}, {new_col})")
                    exit()

            elif current_cell == 'e':  # Game over
                print(f"Game over! ({new_row}, {new_col})")
                exit()

# If there are remaining commands and no end conditions were met
remaining_coal = total_coal - collected_coal
print(f"{remaining_coal} pieces of coal left. ({miner_position[0]}, {miner_position[1]})")
