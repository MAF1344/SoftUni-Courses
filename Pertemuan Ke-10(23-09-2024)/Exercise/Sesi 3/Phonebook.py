# Dictionary to store phonebook entries
phonebook = {}

# Read entries for the phonebook
while True:
    entry = input().strip()
    if entry.isdigit():
        # If the input is a number, it indicates the number of searches to perform
        num_queries = int(entry)
        break
    name, number = entry.split('-')
    phonebook[name] = number

# Perform searches based on the input number of queries
for _ in range(num_queries):
    query = input().strip()
    if query in phonebook:
        print(f"{query} -> {phonebook[query]}")
    else:
        print(f"Contact {query} does not exist.")
