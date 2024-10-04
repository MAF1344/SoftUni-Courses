from collections import deque

def santa_present_factory():
    # User input
    materials = list(map(int, input().split()))
    magic_levels = deque(map(int, input().split()))

    presents = {"Doll": 150, "Wooden train": 250, "Teddy bear": 300, "Bicycle": 400}
    crafted_presents = {}

    while materials and magic_levels:
        material = materials.pop()
        magic = magic_levels.popleft()

        if material == 0 or magic == 0:
            # If either material or magic is zero, continue to the next pair
            if material != 0:
                materials.append(material)
            if magic != 0:
                magic_levels.appendleft(magic)
            continue

        result = material * magic

        if result in presents.values():
            present = [name for name, level in presents.items() if level == result][0]
            if present in crafted_presents:
                crafted_presents[present] += 1
            else:
                crafted_presents[present] = 1
        elif result < 0:
            # If the result is negative, sum the values and add the result to materials
            materials.append(material + magic)
        else:
            # If the result is positive and not a match, remove only the magic and increase material by 15
            materials.append(material + 15)

    # Check if the necessary presents were crafted
    if ("Doll" in crafted_presents and "Wooden train" in crafted_presents) or \
       ("Teddy bear" in crafted_presents and "Bicycle" in crafted_presents):
        print("The presents are crafted! Merry Christmas!")
    else:
        print("No presents this Christmas!")

    if materials:
        print(f"Materials left:", end=" ")
        for i in range(len(materials) - 1, -1, -1):
            if i == 0:
                print(materials[i])
            else:
                print(materials[i], end=", ")
    if magic_levels:
        print(f"Magic left: {', '.join(map(str, magic_levels))}")

    for present, count in sorted(crafted_presents.items()):
        print(f"{present}: {count}")

# Example usage
santa_present_factory()
