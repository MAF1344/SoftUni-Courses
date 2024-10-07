def age_assignment(*names, **age_dict):
    # Step 1: Create a dictionary to hold the name-age assignments
    name_age = {}

    # Step 2: Assign ages based on the first letter of each name
    for name in names:
        first_letter = name[0]  # Get the first letter of the name
        if first_letter in age_dict:  # Check if the letter exists in the age dictionary
            name_age[name] = age_dict[first_letter]  # Assign the age to the name

    # Step 3: Sort names alphabetically
    sorted_names = sorted(name_age.keys())

    # Step 4: Create the output string
    output_lines = [f"{name} is {name_age[name]} years old." for name in sorted_names]

    return '\n'.join(output_lines)


# Example usage
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))