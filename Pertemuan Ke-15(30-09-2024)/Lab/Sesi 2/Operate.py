def operate(operator, *args):
    def addition(a, b):
        return a + b
    def subtraction(a, b):
        return a - b
    def multiplication(a, b):
        return a * b
    def division(a, b):
        return a / b

    if operator == "+":
        result = args[0]
        for num in args[1:]:
            result = addition(result, num)
    elif operator == "-":
        result = args[0]
        for num in args[1:]:
            result = subtraction(result, num)
    elif operator == "*":
        result = args[0]
        for num in args[1:]:
            result = multiplication(result, num)
    elif operator == "/":
        result = args[0]
        for num in args[1:]:
            result = division(result, num)
    else:
        return "Invalid operator"

    return result