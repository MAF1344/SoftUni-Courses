import re

data = input().upper()
matches = re.findall(r'(\D+)(\d+)', data)

result = []
for string, count in matches:
    result.append(string * int(count))

rage_message = ''.join(result)
unique_symbols = len(set(rage_message))

print(f"Unique symbols used: {unique_symbols}")
print(rage_message)
