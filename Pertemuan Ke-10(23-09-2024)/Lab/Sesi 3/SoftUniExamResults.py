results = {}
submissions = {}

while True:
    command = input()
    if command == "exam finished":
        break

    if "banned" in command:
        username = command.split("-")[0]
        if username in results:
            del results[username]
    else:
        username, language, points = command.split("-")
        points = int(points)

        if username not in results:
            results[username] = {}
        if language not in results[username]:
            results[username][language] = points
        else:
            results[username][language] = max(results[username][language], points)

        if language not in submissions:
            submissions[language] = 0
        submissions[language] += 1

print("Results:")
for username, languages in results.items():
    for language, points in languages.items():
        print(f"{username} | {points}")

print("Submissions:")
for language, count in submissions.items():
    print(f"{language} - {count}")