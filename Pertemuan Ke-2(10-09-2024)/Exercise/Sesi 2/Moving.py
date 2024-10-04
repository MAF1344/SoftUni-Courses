w = int(input())
l = int(input())
h = int(input())
space = w * l * h
stuff_volume = 0

while True:
    stuff = input()
    if stuff == 'Done':
        break

    stuff = int(stuff)
    stuff_volume += stuff

    if stuff_volume >= space:
        break

if space >= stuff_volume:
    print(f"{space - stuff_volume} Cubic meters left.")
else:
    print(f"No more free space! You need {stuff_volume - space} Cubic meters more.")