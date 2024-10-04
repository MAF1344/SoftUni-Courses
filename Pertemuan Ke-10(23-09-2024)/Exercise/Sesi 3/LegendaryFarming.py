# Initialize the dictionary for key materials and junk
materials = {'shards': 0, 'fragments': 0, 'motes': 0}
junk = {}

# Define the thresholds and corresponding items
legendary_items = {
    'shadowmourne': 250,
    'valanyr': 250,
    'dragonwrath': 250
}

# Process the input lines
while True:
    try:
        line = input().strip()
    except EOFError:
        break

    # Split the line into parts
    parts = line.split()

    # Iterate through each material and quantity
    for i in range(0, len(parts), 2):
        quantity = int(parts[i])
        material = parts[i + 1].lower()

        if material in materials:
            materials[material] += quantity
            # Check if any legendary item can be obtained
            for item, threshold in legendary_items.items():
                if materials[material] >= threshold:
                    print(f"{item.capitalize()} obtained!")
                    materials[material] -= threshold
                    break
            if materials[material] >= threshold:
                break
        else:
            if material not in junk:
                junk[material] = 0
            junk[material] += quantity

# Print remaining key materials
for material in ['shards', 'fragments', 'motes']:
    print(f"{material}: {materials[material]}")

# Print junk items in the order of appearance
for item, quantity in junk.items():
    print(f"{item}: {quantity}")
