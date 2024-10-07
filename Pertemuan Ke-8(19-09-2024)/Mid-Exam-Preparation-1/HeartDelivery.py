# Input: neighborhood as string of even integers separated by "@"
neighborhood = list(map(int, input().split('@')))

cupid_position = 0
house_count = len(neighborhood)

while True:
    command = input()

    if command == 'Love!':
        break

    # Parsing the jump length
    jump = int(command.split()[1])

    # Moving Cupid
    cupid_position += jump

    # If Cupid jumps outside the neighborhood, he returns to the first house (index 0)
    if cupid_position >= len(neighborhood):
        cupid_position = 0

    # Decrease needed hearts by 2
    if neighborhood[cupid_position] == 0:
        print(f"Place {cupid_position} already had Valentine's day.")
    else:
        neighborhood[cupid_position] -= 2
        if neighborhood[cupid_position] == 0:
            print(f"Place {cupid_position} has Valentine's day.")
            house_count -= 1

# Output Cupid's last position
print(f"Cupid's last position was {cupid_position}.")

# Check if all houses have had Valentine's day
if house_count == 0:
    print("Mission was successful.")
else:
    print(f"Cupid has failed {house_count} places.")
