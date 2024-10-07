prime_sum = 0
non_prime_sum = 0

while True:
    inp = input()

    if inp.lower() == 'stop':
        break

    try:
        num = int(inp)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        continue

    if num < 0:
        print('Number is negative.')
        continue

    if num <= 1:
        is_prime = False
    elif num == 2:
        is_prime = True
    elif num % 2 == 0:
        is_prime = False
    else:
        is_prime = True
        for i in range(3, int(num ** 0.5) + 1, 2):
            if num % i == 0:
                is_prime = False
                break

    if is_prime:
        prime_sum += num
    else:
        non_prime_sum += num

print(f"Sum of all prime numbers is: {prime_sum}")
print(f"Sum of all non prime numbers is: {non_prime_sum}")
