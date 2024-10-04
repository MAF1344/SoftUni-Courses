import math

days = int(input())
foods = int(input())
deer1 = float(input())
deer2 = float(input())
deer3 = float(input())

food_needed = (days * deer1) + (days * deer2) + (days * deer3)

if foods >= food_needed:
    remaining_food = foods - food_needed
    print(f"{math.floor(remaining_food)} kilos of food left.")
else:
    food_shortage = food_needed - foods
    print(f"{math.ceil(food_shortage)} more kilos of food are needed.")
