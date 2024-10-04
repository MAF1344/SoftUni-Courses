n = int(input())
space_left = 0
game_on = True

for i in range(n):
    chairs, required = input().split()
    chairs, required = len(chairs), int(required)

    if chairs < required:
        print(f"{required - chairs} more chairs needed in room {i + 1}")
        game_on = False
    else:
        space_left += (chairs - required)

if game_on:
    print(f"Game On, {space_left} free chairs left")