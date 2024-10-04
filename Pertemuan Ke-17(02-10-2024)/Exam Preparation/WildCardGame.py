def draw_cards(*args, **kwargs):
    # Initialize lists to hold card names
    monster_cards = []
    spell_cards = []

    # Process the positional arguments (tuples)
    for card in args:
        card_name, card_type = card
        if card_type == "monster":
            monster_cards.append(card_name)
        elif card_type == "spell":
            spell_cards.append(card_name)

    # Process the keyword arguments
    for card_name, card_type in kwargs.items():
        if card_type == "monster":
            monster_cards.append(card_name)
        elif card_type == "spell":
            spell_cards.append(card_name)

    # Sort the lists as per requirements
    monster_cards.sort(reverse=True)  # Descending order for monsters
    spell_cards.sort()  # Ascending order for spells

    # Prepare the output
    output = []

    # Add monster cards if they exist
    if monster_cards:
        output.append("Monster cards:")
        for name in monster_cards:
            output.append(f"  ***{name}")

    # Add spell cards if they exist
    if spell_cards:
        output.append("Spell cards:")
        for name in spell_cards:
            output.append(f"  $$${name}")

    # Join the output list into a single string with new lines
    return "\n".join(output)


# Example usage
print(draw_cards(("cyber dragon", "monster"), freeze="spell",))
print()

print(draw_cards(("celtic guardian", "monster"), ("earthquake", "spell"), ("fireball", "spell"), raigeki="spell", destroy="spell",))
print()

print(draw_cards(("brave attack", "spell"), ("freeze", "spell"), lightning_bolt="spell", fireball="spell",))