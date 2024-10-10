def even_parameters(func):
    def wrapper(*args):
        if all(isinstance(arg, int) and arg % 2 == 0 for arg in args):
            return func(*args)
        return "Please use only even numbers!"
    return wrapper

@even_parameters
def add(a, b):
    return a + b

@even_parameters
def multiply(*nums):
    result = 1
    for num in nums:
        result *= num
    return result

