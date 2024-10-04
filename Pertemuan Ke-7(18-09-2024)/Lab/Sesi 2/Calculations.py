input_operator = input()
fnum = int(input())
snum = int(input())

def solve(a, b, operator):
    result = None
    if operator == 'multiply':
        result = a * b
    elif operator == 'divide':
        result = int(a / b)
    elif operator == 'add':
        result = a + b
    if operator == 'subtract':
        result = a - b
    return result

print(solve(fnum, snum, input_operator))