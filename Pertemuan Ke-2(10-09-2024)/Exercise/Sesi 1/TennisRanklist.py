tournaments = int(input())
points = int(input())
final_point = 0
win = 0

for i in range(0, tournaments):
    stage = input()

    if stage == 'W':
        final_point += 2000
        win += 1
    elif stage == "F":
        final_point += 1200
    elif stage == "SF":
        final_point += 720

print(f"Final points: {final_point + points}")
print(f"Average points: {int(final_point / tournaments)}")
print(f"{(win / tournaments) * 100:.2f}%")