number = int(input())
number = list(str(number))

def odd_and_even_sum(a):
    even = 0
    odd = 0

    for i in range(len(a)):
        a[i] = int(a[i])

        if a[i] % 2 == 0:
            even += a[i]
        else:
            odd += a[i]

    print(f"Odd sum = {odd}, Even sum = {even}")

odd_and_even_sum(number)