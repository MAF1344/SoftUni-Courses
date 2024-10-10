def type_check(expected_type):
    def decorator(func):
        def wrapper(arg):
            if isinstance(arg, expected_type):
                return func(arg)
            return "Bad Type"
        return wrapper
    return decorator

@type_check(int)
def times2(num):
    return num * 2

@type_check(str)
def first_letter(word):
    return word[0]
