n = int(input())

positive = []
negative = []

negative_sum = 0

for i in range(n):
    number = int(input())
    if number > -1:
        positive.append(number)
    elif number < 0:
        negative.append(number)
        negative_sum += number

print(positive)
print(negative)
print(f"Count of positives: {len(positive)}")
print(f"Sum of negatives: {negative_sum}")