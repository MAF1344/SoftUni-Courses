def even_odd_filter(**kwargs):
    result = {}

    # Process the named arguments
    for key, value in kwargs.items():
        if key == "even":
            result[key] = [num for num in value if num % 2 == 0]
        elif key == "odd":
            result[key] = [num for num in value if num % 2 != 0]

    # Sort the dictionary by the length of lists in descending order
    sorted_result = dict(sorted(result.items(), key=lambda item: len(item[1]), reverse=True))

    return sorted_result


# Example usage
filtered_numbers = even_odd_filter(even=[1, 2, 3, 4, 5, 6], odd=[1, 3, 5, 6, 8, 10])
print(filtered_numbers)
# Output: {'even': [2, 4, 6], 'odd': [1, 3, 5]}

print(even_odd_filter(
    odd=[2, 2, 30, 44, 10, 5],
))
