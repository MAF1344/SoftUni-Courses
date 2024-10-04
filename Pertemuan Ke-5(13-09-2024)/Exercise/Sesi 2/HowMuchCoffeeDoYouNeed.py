coffee = 0

while True:
    event = input()

    if event == 'END':
        break

    if event.lower() in ['coding', 'dog', 'cat', 'movie']:
        if event.islower():
            coffee += 1
        elif event.isupper():
            coffee += 2

if coffee <= 5:
    print(coffee)
else:
    print("You need extra sleep")
