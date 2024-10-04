def separate_and_sum(numbers):
  negatives = []
  positives = []

  for num in numbers:
    if num < 0:
      negatives.append(num)
    else:
      positives.append(num)

  sum_negatives = sum(negatives)
  sum_positives = sum(positives)

  if abs(sum_negatives) > sum_positives:
    result = "The negatives are stronger than the positives"
  else:
    result = "The positives are stronger than the negatives"

  return sum_negatives, sum_positives, result

# Get input from the user
numbers = input().split()
numbers = [int(num) for num in numbers]

# Process the input and print the results
sum_negatives, sum_positives, result = separate_and_sum(numbers)

print(sum_negatives)
print(sum_positives)
print(result)