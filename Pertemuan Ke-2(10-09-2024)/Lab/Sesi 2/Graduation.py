name = input()
total = 0
exclude = 12
failed_grades = 0
current_grade = 1

while current_grade <= 12:
    grade = float(input())

    if grade < 4:
        failed_grades += 1
        if failed_grades == 2:
            print(f"{name} has been excluded at {current_grade} grade")
            break
    else:
        total += grade
        current_grade += 1

    if current_grade > 12:
        avg = total / 12
        print(f"{name} graduated. Average grade: {avg:.2f}")