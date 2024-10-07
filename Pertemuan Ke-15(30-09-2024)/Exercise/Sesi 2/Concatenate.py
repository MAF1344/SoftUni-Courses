def concatenate(*args, **kwargs):
    # Step 1: Concatenate all string arguments
    result = ''.join(args)

    # Step 2: Replace occurrences of each key with its corresponding value
    for key, value in kwargs.items():
        result = result.replace(key, value)

    return result


print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))