username = input().split(", ")
for name in username:
    if name.isalnum() and 3 < len(name) < 16 or "-" in name:
        print(name)