def inventory():
    items = input().split(", ")

    while True:
        command = input()
        if command == "Craft!":
            print(", ".join(items))
            break

        action, item = command.split(" - ")

        if action == "Collect":
            if item not in items:
                items.append(item)
        elif action == "Drop":
            if item in items:
                items.remove(item)
        elif action == "Combine Items":
            old_item, new_item = item.split(":")
            if old_item in items:
                index = items.index(old_item)
                items.insert(index + 1, new_item)
        elif action == "Renew":
            if item in items:
                items.remove(item)
                items.append(item)

inventory()