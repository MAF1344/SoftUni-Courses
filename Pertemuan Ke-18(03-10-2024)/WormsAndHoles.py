def match_worms_and_holes(worms, holes):
    matches = 0
    worm_in = 0
    while worms and holes:
        worm = worms.pop()
        worm_in += 1
        hole = holes.pop(0)
        if worm == hole:
            matches += 1
        else:
            worm -= 3
            if worm <= 0:
                continue
            worms.append(worm)

    if matches > 0:
        print(f"Matches: {matches}")
    else:
        print("There are no matches.")

    if not worms:
        if matches == worm_in:
            print("Every worm found a suitable hole!")
        else:
            print("Worms left: none")
    else:
        print(f"Worms left: {', '.join(map(str, worms))}")

    if not holes:
        print("Holes left: none")
    else:
        print(f"Holes left: {', '.join(map(str, holes))}")

# Get input from the user
worm_input = input().split()
hole_input = input().split()

# Convert input to integers
worms = [int(worm) for worm in worm_input]
holes = [int(hole) for hole in hole_input]

# Call the function to match worms and holes
match_worms_and_holes(worms, holes)