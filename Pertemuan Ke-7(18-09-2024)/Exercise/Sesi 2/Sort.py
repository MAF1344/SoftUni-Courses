numbers = input()
def sort(number):
    number = list(map(int, number.split()))
    print(sorted(number))

sort(numbers)