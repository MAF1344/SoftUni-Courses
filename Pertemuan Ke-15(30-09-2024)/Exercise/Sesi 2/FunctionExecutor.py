def func_executor(*args):
    results = []

    for func, params in args:
        result = func(*params)  # Execute the function with its arguments
        results.append(f"{func.__name__} - {result}")  # Format the result

    return "\n".join(results)


# Example functions to demonstrate usage
def sum_numbers(num1, num2):
    return num1 + num2


def multiply_numbers(num1, num2):
    return num1 * num2


print(func_executor(
    (sum_numbers, (1, 2)),
    (multiply_numbers, (2, 4))
))
