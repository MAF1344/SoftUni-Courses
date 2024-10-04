nylon = (int(input()) + 2) * 1.50
paint = int(input())
detergent = int(input()) * 5.00
bags = 0.40
material = nylon + ((paint + (paint * (10/100))) * 14.50) + detergent + bags
hours = int(input()) * (material * (30/100))

print(f"Total Cost : {material + hours}")
