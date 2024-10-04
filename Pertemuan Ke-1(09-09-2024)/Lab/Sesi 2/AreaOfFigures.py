from math import pi
shape = str(input())

if shape == 'square':
    x = float(input())
    print(x * x)
elif shape == 'rectangle':
    x = float(input())
    y = float(input())
    print(x * y)
elif shape == 'circle':
    x = float(input())
    print(pi * x * x)
elif shape == 'triangle':
    x = float(input())
    y = float(input())
    print((x * y) / 2)
else:
    print("Shape Doesn't Exist")