import re

tickets = [ticket.strip() for ticket in input().split(", ")]

for ticket in tickets:
    if len(ticket) != 20:
        print(f"invalid ticket")
        continue

    left_half = ticket[:10]
    right_half = ticket[10:]

    match = re.search(r'(@{6,10}|#{6,10}|\${6,10}|\^{6,10})', left_half)
    if match:
        match_symbol = match.group(0)[0]
        left_count = len(match.group(0))
        right_count = len(re.search(f'({match_symbol}{{6,10}})', right_half).group(0))

        if left_count == 10 and right_count == 10:
            print(f'ticket "{ticket}" - 10{match_symbol} Jackpot!')
        else:
            print(f'ticket "{ticket}" - {min(left_count, right_count)}{match_symbol}')
    else:
        print(f'ticket "{ticket}" - no match')