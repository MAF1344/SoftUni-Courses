guests = {}

while True:
    command = input()
    if command == "Stop":
        break

    appetite, name, meal = command.split("-")

    if appetite == "Like":
        # Tambahkan tamu baru jika belum ada
        if name not in guests:
            guests[name] = {"liked_meal": [], "disliked_meal": []}
        # Tambahkan makanan ke liked_meal jika belum ada
        if meal not in guests[name]["liked_meal"]:
            guests[name]["liked_meal"].append(meal)

    elif appetite == "Dislike":
        # Cek apakah tamu ada di pesta
        if name not in guests:
            print(f"{name} is not at the party.")
        else:
            # Cek apakah makanan ada di liked_meal tamu
            if meal in guests[name]["liked_meal"]:
                guests[name]["liked_meal"].remove(meal)
                guests[name]["disliked_meal"].append(meal)
                print(f"{name} doesn't like the {meal}.")
            else:
                print(f"{name} doesn't have the {meal} in his/her collection.")

# Output hasil akhir
for guest, meals in guests.items():
    liked_meals = ", ".join(meals['liked_meal'])
    print(f"{guest}: {liked_meals}")

# Hitung total makanan yang tidak disukai
total_unliked_meals = sum(len(meals['disliked_meal']) for meals in guests.values())
print(f"Unliked meals: {total_unliked_meals}")