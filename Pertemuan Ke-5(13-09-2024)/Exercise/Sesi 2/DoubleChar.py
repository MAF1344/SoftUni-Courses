while True:
    text = input()

    if text == 'End':
        break
    elif text == 'SoftUni':
        continue
    else:
        for char in text:
            print(char * 2, end='')
        print()