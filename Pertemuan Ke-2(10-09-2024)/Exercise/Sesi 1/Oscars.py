actor = input()
point = float(input())
assessors = int(input())

for i in range(assessors):
    assessors_name = input()
    assessors_score = float(input())

    point += (len(assessors_name) * assessors_score) / 2

    if point >= 1250.5:
        break

if point >= 1250.05:
    print(f"Congratulations, {actor} got a nominee for leading role with {point:.1f}!")
else:
    needed_points = 1250.5 - point
    print(f"Sorry, {actor} you need {needed_points:.1f} more!")
