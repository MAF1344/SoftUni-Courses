count = int(input())
students = {}
order = []

for _ in range(count):
    line = input().split()
    student, grade = line
    if student not in students:
        students[student] = []
        order.append(student)
    students[student].append(float(grade))

for student in order:
    grades_str = ' '.join(f"{grade:.2f}" for grade in students[student])
    avg_grade = sum(students[student]) / len(students[student])
    print(f"{student} -> {grades_str} (avg: {avg_grade:.2f})")