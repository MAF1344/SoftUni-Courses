name = input()

while True:
    command = input()
    if command == "Registration":
        break

    tokens = command.split()
    action = tokens[0]

    if action == "Letters":
        if tokens[1] == "Lower":
            name = name.lower()
            print(name)
        elif tokens[1] == "Upper":
            name = name.upper()
            print(name)

    elif action == "Reverse":
        start = int(tokens[1])
        end = int(tokens[2])
        if 0 <= start < len(name) and 0 <= end < len(name) and start <= end:
            substring = name[start:end + 1]
            reversed_substring = substring[::-1]
            print(reversed_substring)

    elif action == "Substring":
        substring = tokens[1]
        if substring in name:
            name = name.replace(substring, "", 1)
            print(name)
        else:
            print(f"The username {name} doesn't contain {substring}.")

    elif action == "Replace":
        char = tokens[1]
        name = name.replace(char, "-")
        print(name)

    elif action == "IsValid":
        char = tokens[1]
        if char in name:
            print("Valid username.")
        else:
            print(f"{char} must be contained in your username.")