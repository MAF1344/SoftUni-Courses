num1 = int(input())
num2 = int(input())
num3 = int(input())

smallest_num = lambda a, b, c: min(a, b, c)

print(smallest_num(num1, num2, num3))