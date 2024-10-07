import re

total_cost = 0
furniture = []

while True:
    line = input()
    if line == "Purchase":
        break
    match = re.match(r'>>([A-Za-z\s]+)<<(\d+\.?\d*)!(\d+)', line)
    if match:
        name, price, quantity = match.groups()
        furniture.append(name)
        total_cost += float(price) * int(quantity)

print("Bought furniture:")
for item in furniture:
    print(item)
print(f"Total money spend: {total_cost:.2f}")