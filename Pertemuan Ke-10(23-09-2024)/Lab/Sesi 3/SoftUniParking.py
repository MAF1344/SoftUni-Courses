n = int(input())
parking_member = {}

for i in range(n):
    command = input().split()
    action = command[0]
    username = command[1]

    if action == 'register':
        plate_number = command[2]
        if username in parking_member:
            print(f"ERROR: already registered with plate number {parking_member[username]}")
        else:
            parking_member[username] = plate_number
            print(f"{username} registered {plate_number} successfully")
    elif action == 'unregister':
        if username not in parking_member:
            print(f"ERROR: user {username} not found")
        else:
            del parking_member[username]
            print(f"{username} unregistered successfully")
    else:
        print("Error")

for username, plate_number in parking_member.items():
    print(f"{username} => {plate_number}")
