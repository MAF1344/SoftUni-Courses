n = int(input())
students = {}

for _ in range(n):
    name = input().strip()
    grade = float(input().strip())

    if name not in students:
        students[name] = []
    students[name].append(grade)

for name, grades in students.items():
    average_grade = sum(grades) / len(grades)
    if average_grade >= 4.50:
        print(f"{name} -> {average_grade:.2f}")