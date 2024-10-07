import math

number1 = int(input())
number2 = int(input())

def factorial_division(num1, num2):
    fact1 = math.factorial(num1)
    fact2 = math.factorial(num2)
    result = fact1 / fact2
    return f"{result:.2f}"

print(factorial_division(number1, number2))