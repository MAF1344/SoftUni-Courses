import re

while True:
    line = input()
    if not line:
        break
    matches = re.findall(r'\d+', line)
    if matches:
        print(' '.join(matches), end=' ')