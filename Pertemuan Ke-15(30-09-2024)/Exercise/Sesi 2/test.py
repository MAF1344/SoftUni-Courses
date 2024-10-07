def even_odd(*args):
    # Get the last argument as the command
    command = args[-1]

    # Filter the numbers based on the command
    if command == "even":
        return [num for num in args[:-1] if num % 2 == 0]
    elif command == "odd":
        return [num for num in args[:-1] if num % 2 != 0]
    else:
        return []  # Return an empty list if the command is invalid


# Example usage
result = even_odd(1, 2, 3, 4, 5, "even")
print(result)  # Output: [2, 4]

result = even_odd(1, 2, 3, 4, 5, "odd")
print(result)  # Output: [1, 3, 5]
