chicken = int(input()) * 10.35
fish = int(input()) * 12.40
vegetarian = int(input()) * 8.15
dessert = (chicken + fish + vegetarian) * (20/100)
totalMenu = chicken + fish + vegetarian + dessert
delivery = 2.50

print(f"Total Cost: {totalMenu + delivery}")