def softuni_students(*args, **kwargs):
    valid_students = []
    invalid_students = []

    # Step 1: Create a dictionary of valid course IDs and names
    courses = {}
    for course_id, course_name in kwargs.items():
        courses[course_id] = course_name

    # Step 2: Sort through the provided student-course ID tuples
    students = {}
    for course_id, username in args:
        if course_id in courses:
            # If the student's course ID is valid, associate them with the course
            students[username] = courses[course_id]
        else:
            # If the course ID is invalid, add to the invalid list
            invalid_students.append(username)

    # Step 3: Prepare the result output
    sorted_usernames = sorted(students.keys())
    for username in sorted_usernames:
        valid_students.append(
            f"*** A student with the username {username} has successfully finished the course {students[username]}!")

    if invalid_students:
        valid_students.append(f"!!! Invalid course students: {', '.join(sorted(invalid_students))}")

    # Step 4: Return the final result as a single string
    return '\n'.join(valid_students)


print(softuni_students(
    ('id_1', 'Kaloyan9905'),
    id_1='Python Web Framework',
))
print()
print(softuni_students(
    ('id_7', 'Silvester1'),
    ('id_32', 'Katq21'),
    ('id_7', 'The programmer'),
    id_76='Spring Fundamentals',
    id_7='Spring Advanced',
))
print()
print(softuni_students(
    ('id_22', 'Programmingkitten'),
    ('id_11', 'MitkoTheDark'),
    ('id_321', 'Bobosa253'),
    ('id_08', 'KrasimirAtanasov'),
    ('id_32', 'DaniBG'),
    id_321='HTML & CSS',
    id_22='Machine Learning',
    id_08='JS Advanced',
))
