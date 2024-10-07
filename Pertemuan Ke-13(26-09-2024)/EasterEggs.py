import re


def find_easter_eggs(text):
    # Regular expression for matching egg color and amount
    pattern = r'[@#]+([a-z]{3,})[@#]+[^a-z0-9]*\/(\d+)\/'

    # Find all matches based on the pattern
    matches = re.findall(pattern, text)

    # Loop through the matches and print the results
    for color, amount in matches:
        print(f'You found {amount} {color} eggs!')

# Function calls
find_easter_eggs(input())