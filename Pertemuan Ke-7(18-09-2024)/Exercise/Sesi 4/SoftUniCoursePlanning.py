def course_planning():
    # Membaca jadwal awal
    initial_schedule = input().split(", ")
    commands = []
    while True:
        command = input()
        if command == "course start":
            break
        commands.append(command)

    schedule = initial_schedule
    while commands:
        cmd = commands.pop(0).split(":")
        if cmd[0] == "Add" and cmd[1] not in schedule:
            schedule.append(cmd[1])
        elif cmd[0] == "Insert" and cmd[1] not in schedule:
            schedule.insert(int(cmd[2]), cmd[1])
        elif cmd[0] == "Remove" and cmd[1] in schedule:
            lesson = cmd[1]
            if lesson in schedule:
                schedule.remove(lesson)
                exercise = f"{lesson}-Exercise"
                if exercise in schedule:
                    schedule.remove(exercise)
        elif cmd[0] == "Swap":
            if cmd[1] in schedule and cmd[2] in schedule:
                i1, i2 = schedule.index(cmd[1]), schedule.index(cmd[2])
                schedule[i1], schedule[i2] = schedule[i2], schedule[i1]
                # Swap any exercises if they exist
                if f"{cmd[1]}-Exercise" in schedule:
                    exercise1_idx = schedule.index(f"{cmd[1]}-Exercise")
                    schedule.insert(i2 + 1, schedule.pop(exercise1_idx))
                if f"{cmd[2]}-Exercise" in schedule:
                    exercise2_idx = schedule.index(f"{cmd[2]}-Exercise")
                    schedule.insert(i1 + 1, schedule.pop(exercise2_idx))
        elif cmd[0] == "Exercise":
            lesson = cmd[1]
            exercise = f"{lesson}-Exercise"
            if lesson in schedule:
                # Tambahkan exercise jika belum ada
                lesson_index = schedule.index(lesson)
                if exercise not in schedule:
                    schedule.insert(lesson_index + 1, exercise)
            else:
                # Jika pelajaran tidak ada, tambahkan di akhir dengan exercise
                schedule.append(lesson)
                schedule.append(exercise)

    # Cetak hasil akhir
    for idx, lesson in enumerate(schedule):
        print(f"{idx+1}.{lesson}")

# Example usage:
course_planning()
