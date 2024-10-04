days = int(input())
food = float(input())
eaten_food = 0
dog_food = 0
cat_food = 0
biscuits = 0

for i in range(0, days):
    dog = int(input())
    cat = int(input())

    if (i + 1) % 3 == 0:
        daily_biscuits = (dog + cat) * 10 / 100
        biscuits += daily_biscuits

    dog_food += dog
    cat_food += cat
    eaten_food += dog + cat

print(f"Total eaten biscuits: {round(biscuits)}gr.")

print(f"{(eaten_food / food) * 100:.2f}% of the food has been eaten.")

print(f"{(dog_food / eaten_food) * 100:.2f}% eaten from the dog.")
print(f"{(cat_food / eaten_food) * 100:.2f}% eaten from the cat.")
