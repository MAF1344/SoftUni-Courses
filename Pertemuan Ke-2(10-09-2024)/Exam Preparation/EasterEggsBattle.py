one_eggs = int(input())
two_eggs = int(input())

while True:
    if one_eggs == 0 or two_eggs == 0:
        break

    winner = input()

    if winner == 'End':
        break
    elif winner == 'one':
        two_eggs -= 1
    elif winner == 'two':
        one_eggs -= 1

if one_eggs == 0:
    print(f"Player one is out of eggs. Player two has {two_eggs} eggs left.")
elif two_eggs == 0:
    print(f"Player two is out of eggs. Player one has {one_eggs} eggs left.")
else:
    print(f"Player one has {one_eggs} eggs left.")
    print(f"Player two has {two_eggs} eggs left.")