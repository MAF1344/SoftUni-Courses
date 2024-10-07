text = input()

while True:
    command = input()
    if command == "End":
        break
    tokens = command.split()
    if tokens[0] == "Translate":
        text = text.replace(tokens[1], tokens[2])
        print(text)
    elif tokens[0] == "Includes":
        if tokens[1] in text:
            print(True)
        else:
            print(False)
    elif tokens[0] == "Start":
        if text.startswith(tokens[1]):
            print(True)
        else:
            print(False)
    elif tokens[0] == "Lowercase":
        text = text.lower()
        print(text)
    elif tokens[0] == "FindIndex":
        search_char = tokens[1].lower()
        for i in range(len(text) - 1, -1, -1):
            if search_char == text[i].lower():
                print(i)
                break
    elif tokens[0] == "Remove":
        index_to_remove = int(tokens[1])
        num_chars_to_remove = int(tokens[2])
        if 0 <= index_to_remove < len(text):
            end_index = min(index_to_remove + num_chars_to_remove, len(text))
            text = text[:index_to_remove] + text[end_index:]
            print(text)