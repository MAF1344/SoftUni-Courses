def grocery_store(**kwargs):
    # Step 1: Sort products by quantity (descending), name length (descending), and name (ascending)
    sorted_products = sorted(
        kwargs.items(),
        key=lambda item: (-item[1], -len(item[0]), item[0])
    )

    # Step 2: Format the receipt string
    receipt_lines = [f"{product}: {quantity}" for product, quantity in sorted_products]
    return '\n'.join(receipt_lines)

# Example usage
print(grocery_store(
    bread=2,
    pasta=2,
    eggs=20,
    carrot=1,
))
