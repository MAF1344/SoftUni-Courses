numbers = input()

def evenNum(x):
    x = list(map(int, x.split()))
    even = list(filter(lambda num: num % 2 == 0, x))
    print(even)

evenNum(numbers)