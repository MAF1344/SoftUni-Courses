numbers = input().split()

def rounded_number(a):
    rounded_numbers = []
    for i in range(len(a)):
        numbers_int = round(float(a[i]))
        rounded_numbers.append(numbers_int)

    return rounded_numbers

print(rounded_number(numbers))