n = int(input())
best_value = 0
best_snowball = ""

for _ in range(n):
    weight = int(input())
    time = int(input())
    quality = int(input())

    value = (weight / time) ** quality

    if value > best_value:
        best_value = value
        best_snowball = f"{weight} : {time} = {int(value)} ({quality})"

print(best_snowball)