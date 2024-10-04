budget = float(input())
flour_price = float(input())

egg_price = flour_price * 75/100
milk_price_per_liter = flour_price * 125/100
milk_price_per_loaf = milk_price_per_liter / 4

loaf_price = flour_price + egg_price + milk_price_per_loaf

loaves_made = 0
colored_eggs = 0

while budget >= loaf_price:
    loaves_made += 1
    budget -= loaf_price
    colored_eggs += 3

    if loaves_made % 3 == 0:
        colored_eggs -= (loaves_made - 2)

print(f"You made {loaves_made} loaves of Easter bread! Now you have {colored_eggs} eggs and ${budget:.2f} left.")
