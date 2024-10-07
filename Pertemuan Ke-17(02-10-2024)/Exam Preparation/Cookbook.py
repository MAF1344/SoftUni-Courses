def cookbook(*recipes):
    cookbook_recipes = {}

    # Process each recipe
    for recipe_name, cuisine, ingredients in recipes:
        if cuisine not in cookbook_recipes:
            cookbook_recipes[cuisine] = []
        cookbook_recipes[cuisine].append((recipe_name, ingredients))

    # Sort cuisines first by the number of recipes (descending), then by cuisine name (ascending)
    sorted_cuisines = sorted(cookbook_recipes.items(), key=lambda x: (-len(x[1]), x[0]))

    # Result output collection
    result = []

    # Print each cuisine and its recipes
    for cuisine, recipe_list in sorted_cuisines:
        result.append(f"{cuisine} cuisine contains {len(recipe_list)} recipes:")

        # Sort recipes alphabetically by recipe name within each cuisine
        for recipe_name, ingredients in sorted(recipe_list):
            ingredients_str = ", ".join(ingredients)
            result.append(f"  * {recipe_name} -> Ingredients: {ingredients_str}")

    # Return the result as a string, each part joined by newline for proper formatting
    return "\n".join(result)


# Test with the provided case
print(cookbook(
    ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
    ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
    ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
    ("Croissant", "French", ["flour", "butter", "yeast"]),
    ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"])
))

print(cookbook(
    ("Pad Thai", "Thai", ["rice noodles", "shrimp", "peanuts", "bean sprouts", "tamarind sauce"])
))

print(cookbook(
    ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
    ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
    ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
    ("Croissant", "French", ["flour", "butter", "yeast"]),
    ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"]),
    ("Sushi Rolls", "Japanese", ["rice", "nori", "fish", "vegetables"]),
    ("Miso Soup", "Japanese", ["tofu", "seaweed", "green onions"]),
    ("Guacamole", "Mexican", ["avocado", "tomato", "onion", "lime"])
))


