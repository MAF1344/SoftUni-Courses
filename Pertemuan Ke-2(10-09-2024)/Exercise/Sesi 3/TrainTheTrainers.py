jury = int(input())
presentation_count = 0
total_score = 0

while True:
    presentation = input()

    if presentation == 'Finish':
        break

    total_grade = 0

    for i in range(0, jury):
        grade = float(input())
        total_grade += grade
        total_score += grade
        presentation_count += 1

    print(f"{presentation} - {total_grade / jury:.2f}.")

print(f"Student's final assessment is {total_score / presentation_count:.2f}.")