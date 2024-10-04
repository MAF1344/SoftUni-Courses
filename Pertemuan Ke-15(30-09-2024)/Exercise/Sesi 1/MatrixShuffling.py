# Read rows and columns
rows, columns = map(int, input().split())
matrix = [input().split() for _ in range(rows)]  # Filling the matrix with user input

while True:
    command = input()  # Read the command
    if command == "END":  # Check if the command is "END"
        break

    tokens = command.split()

    # Validate input to ensure the swap command is correct
    if tokens[0] == "swap" and len(tokens) == 5:
        # Get the indices for swapping elements
        row1, col1, row2, col2 = map(int, tokens[1:5])  # Convert indices to integers

        # Check if indices are valid
        if (0 <= row1 < rows) and (0 <= col1 < columns) and (0 <= row2 < rows) and (0 <= col2 < columns):
            # Swap the elements in the matrix
            matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
            # Print the matrix after successful swap
            for row in matrix:
                print(' '.join(row))
        else:
            print("Invalid input!")
    else:
        print("Invalid input!")
