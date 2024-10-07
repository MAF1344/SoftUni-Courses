strings = list(map(int, input().split(", ")))

positive = [digit for digit in strings if digit >= 0]
negative = [digit for digit in strings if digit < 0]
even = [digit for digit in strings if digit % 2 == 0]
odd = [digit for digit in strings if digit % 2 == 1]

def format_list(lst):
    return ', '.join(map(str, lst))

print(f"Positive: {format_list(positive)}")
print(f"Negative: {format_list(negative)}")
print(f"Even: {format_list(even)}")
print(f"Odd: {format_list(odd)}")
