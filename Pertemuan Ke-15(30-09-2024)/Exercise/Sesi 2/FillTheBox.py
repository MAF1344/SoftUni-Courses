def fill_the_box(height, length, width, *cubes):
    # Calculate the volume of the box
    box_volume = height * length * width
    total_cubes = 0

    for cube in cubes:
        if cube == "Finish":
            break
        total_cubes += cube

    # Calculate the remaining space in the box
    remaining_space = box_volume - total_cubes

    # Determine the output message
    if remaining_space > 0:
        return f"There is free space in the box. You could put {remaining_space} more cubes."
    else:
        cubes_left = abs(remaining_space)  # Negative space means cubes left over
        return f"No more free space! You have {cubes_left} more cubes."


# Example test cases
print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
