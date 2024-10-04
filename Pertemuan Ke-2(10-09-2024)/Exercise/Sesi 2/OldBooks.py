book = input()
count = 0

while True:
    other_book = input()
    if other_book == book:
        print(f"You checked {count} books and found it.")
        break
    elif other_book == 'No More Books':
        print("The book you search is not here!")
        print(f"You checked {count} books.")
        break

    count += 1
