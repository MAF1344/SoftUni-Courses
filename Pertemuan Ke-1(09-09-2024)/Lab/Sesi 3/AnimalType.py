animal = input().lower()
animal_type = {
    "dog": "mammal",
    "snake": "reptile",
    "crocodile": "reptile",
    "tortoise": "reptile"
}
print(animal_type.get(animal, "unknown"))