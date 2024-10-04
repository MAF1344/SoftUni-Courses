def find_colors(string):
    # Define main and secondary colors with their requirements
    main_colors = {"red", "yellow", "blue"}
    secondary_colors = {
        "orange": {"red", "yellow"},
        "purple": {"red", "blue"},
        "green": {"yellow", "blue"}
    }

    substrings = string.split()
    found_colors = []

    # Iterate through the substrings until they are empty
    while substrings:
        # Use a flag to check if we found any color in this iteration
        color_found = False

        # Iterate through the substrings with two pointers
        for i in range(len(substrings) - 1):
            first = substrings[i]
            last = substrings[-1]  # Always check with the last substring

            combined = first + last

            if combined in main_colors or combined in secondary_colors:
                # If a valid color is found, add it to found_colors
                found_colors.append(combined)
                # Remove both substrings
                substrings.pop(i)  # Remove first
                substrings.pop()  # Remove last
                color_found = True
                break  # Break the loop to restart checking

        # If no colors were found, remove characters from the first and last substrings
        if not color_found:
            if len(substrings) > 1:
                # Trim the first and last elements
                if len(substrings[0]) > 1:
                    substrings[0] = substrings[0][:-1]  # Trim first substring
                else:
                    substrings.pop(0)  # Remove it if it's reduced to empty

                if len(substrings[-1]) > 1:
                    substrings[-1] = substrings[-1][:-1]  # Trim last substring
                else:
                    substrings.pop()  # Remove it if it's reduced to empty
            elif len(substrings) == 1:
                # If only one substring is left, check and possibly remove it
                if len(substrings[0]) > 1:
                    substrings[0] = substrings[0][:-1]  # Trim it
                else:
                    substrings.pop(0)  # Remove it if it's reduced to empty

    # Final validation of colors based on the found colors
    final_colors = []
    for color in found_colors:
        if color in main_colors:
            final_colors.append(color)
        elif color in secondary_colors:
            # Check if the main colors needed for the secondary color are in found_colors
            if secondary_colors[color].issubset(set(final_colors)):
                final_colors.append(color)

    return final_colors


# Get input from the user
input_string = input("Enter the string: ")

# Find and print the colors
colors_found = find_colors(input_string)
print(colors_found)
