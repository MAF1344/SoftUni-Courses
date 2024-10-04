gifts = input().split()

while True:
    command = input()
    if command == "No Money":
        break

    cmd_parts = command.split()
    action = cmd_parts[0]

    if action == "OutOfStock":
        gift = cmd_parts[1]
        gifts = ["None" if g == gift else g for g in gifts]

    elif action == "Required":
        gift = cmd_parts[1]
        index = int(cmd_parts[2])
        if 0 <= index < len(gifts):
            gifts[index] = gift

    elif action == "JustInCase":
        gift = cmd_parts[1]
        gifts[-1] = gift

print(" ".join([gift for gift in gifts if gift != "None"]))