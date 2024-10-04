course_data = {}

while True:
    line = input().strip()
    if line == "end":
        break
    if " : " not in line:
        continue
    course, student = line.split(" : ")
    if course not in course_data:
        course_data[course] = []
    if student not in course_data[course]:
        course_data[course].append(student)

for course, students in course_data.items():
    print(f"{course}: {len(students)}")
    for student in students:
        print(f"-- {student}")