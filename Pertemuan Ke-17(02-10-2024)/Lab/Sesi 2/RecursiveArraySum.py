def calc_sum(numbers, idx):
    if idx == len(numbers) - 1:
        return numbers[idx]
    return numbers[idx] + calc_sum(numbers, idx + 1)
numbers = list(map(int, input().split()))
print(calc_sum(numbers, 0))