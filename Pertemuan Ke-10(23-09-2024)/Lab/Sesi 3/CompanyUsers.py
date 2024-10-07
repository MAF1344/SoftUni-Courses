companies = {}

while True:
    command = input()
    if command == "End":
        break
    company, employee = command.split(" -> ")
    if company not in companies:
        companies[company] = []
    if employee not in companies[company]:
        companies[company].append(employee)

for company, employee in companies.items():
    print(company)
    for employee_id in employee:
        print(f"-- {employee_id}")