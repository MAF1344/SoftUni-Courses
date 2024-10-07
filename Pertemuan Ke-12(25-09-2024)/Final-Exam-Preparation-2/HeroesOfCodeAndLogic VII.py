def process_commands(heroes, commands):
    for command in commands:
        if command.startswith("CastSpell"):
            _, hero_name, mp_needed, spell_name = command.split(" - ")
            mp_needed = int(mp_needed)
            if hero_name in heroes:
                if heroes[hero_name]['MP'] >= mp_needed:
                    heroes[hero_name]['MP'] -= mp_needed
                    print(f"{hero_name} has successfully cast {spell_name} and now has {heroes[hero_name]['MP']} MP!")
                else:
                    print(f"{hero_name} does not have enough MP to cast {spell_name}!")

        elif command.startswith("TakeDamage"):
            _, hero_name, damage, attacker = command.split(" - ")
            damage = int(damage)
            if hero_name in heroes:
                heroes[hero_name]['HP'] -= damage
                if heroes[hero_name]['HP'] > 0:
                    print(
                        f"{hero_name} was hit for {damage} HP by {attacker} and now has {heroes[hero_name]['HP']} HP left!")
                else:
                    del heroes[hero_name]
                    print(f"{hero_name} has been killed by {attacker}!")

        elif command.startswith("Recharge"):
            _, hero_name, amount = command.split(" - ")
            amount = int(amount)
            if hero_name in heroes:
                max_mp = 200
                current_mp = heroes[hero_name]['MP']
                heroes[hero_name]['MP'] = min(max_mp, current_mp + amount)
                recovered_amount = heroes[hero_name]['MP'] - current_mp
                print(f"{hero_name} recharged for {recovered_amount} MP!")

        elif command.startswith("Heal"):
            _, hero_name, amount = command.split(" - ")
            amount = int(amount)
            if hero_name in heroes:
                max_hp = 100
                current_hp = heroes[hero_name]['HP']
                heroes[hero_name]['HP'] = min(max_hp, current_hp + amount)
                recovered_amount = heroes[hero_name]['HP'] - current_hp
                print(f"{hero_name} healed for {recovered_amount} HP!")


# Read input
import sys

input = sys.stdin.read
data = input().strip().split('\n')

# Read number of heroes
n = int(data[0])
heroes = {}

# Read hero details
for i in range(1, n + 1):
    hero_name, hp, mp = data[i].split()
    heroes[hero_name] = {'HP': int(hp), 'MP': int(mp)}

# Read commands
commands = data[n + 1:]
while commands:
    command = commands.pop(0)
    if command == "End":
        break
    process_commands(heroes, [command])

# Print remaining heroes
for hero_name, stats in heroes.items():
    print(f"{hero_name}")
    print(f"  HP: {stats['HP']}")
    print(f"  MP: {stats['MP']}")