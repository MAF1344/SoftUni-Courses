def calculate(strings):
    num1, sign, num2 = strings.split()
    num1 = float(num1)
    num2 = float(num2)

    if sign == "/":
        print(f"{num1 / num2:.2f}")
    elif sign == "*":
        print(f"{num1 * num2:.2f}")
    elif sign == "-":
        print(f"{num1 - num2:.2f}")
    elif sign == "+":
        print(f"{num1 + num2:.2f}")
    elif sign == "^":
        print(f"{num1 ** num2:.2f}")