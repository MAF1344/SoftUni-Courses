def math_operations(*args, **kwargs):
    # Iterate through the floats in the arguments
    for i, number in enumerate(args):
        # Perform operations based on the index of the number
        if i % 4 == 0:  # Addition for the first element
            kwargs['a'] += number
        elif i % 4 == 1:  # Subtraction for the second element
            kwargs['s'] -= number
        elif i % 4 == 2:  # Division for the third element
            if number != 0:  # Avoid division by zero
                kwargs['d'] /= number
        elif i % 4 == 3:  # Multiplication for the fourth element
            kwargs['m'] *= number

    # Sort the items by value in descending order, then by key in ascending order
    sorted_items = sorted(kwargs.items(), key=lambda x: (-x[1], x[0]))

    # Format the results
    result = []
    for key, value in sorted_items:
        result.append(f"{key}: {value:.1f}")

    return "\n".join(result)

# Example usage
print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))
print()
print(math_operations(-1.0, 0.5, 1.6, 0.5, 6.1, -2.8, 80.0, a=0, s=(-2.3), d=0, m=0))
print()
print(math_operations(6.0, a=0, s=0, d=5, m=0))