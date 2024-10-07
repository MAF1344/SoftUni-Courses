num = int(input())

def is_perfect_number(n):
    divisors = [i for i in range(1, n) if n % i == 0]
    if sum(divisors) == n:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."

print(is_perfect_number(num))