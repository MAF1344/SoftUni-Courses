text = list(input())
symbols = {}

for i in range(len(text)):
    if text[i] not in symbols:
        symbols[text[i]] = 0
    symbols[text[i]] += 1

for symbol in sorted(symbols):
    print(f"{symbol}: {symbols[symbol]} time/s")