group = int(input())
total_ppl = 0

makalu_climber = 0
mont_blanc_climber = 0
kilimanjaro_climber = 0
k2_climber = 0
everest_climber = 0

for i in range(group):
    member = int(input())
    total_ppl += member

    if member <= 5:
        makalu_climber += member
    elif 6 <= member <= 12:
        mont_blanc_climber += member
    elif 13 <= member <= 25:
        kilimanjaro_climber += member
    elif 26 <= member <= 40:
        k2_climber += member
    else:
        everest_climber += member

makalu_percentage = makalu_climber / total_ppl * 100
mont_blanc_percentage = mont_blanc_climber / total_ppl * 100
kilimanjaro_percentage = kilimanjaro_climber / total_ppl * 100
k2_percentage = k2_climber / total_ppl * 100
everest_percentage = everest_climber / total_ppl * 100

print(f"{makalu_percentage:.2f}%")
print(f"{mont_blanc_percentage:.2f}%")
print(f"{kilimanjaro_percentage:.2f}%")
print(f"{k2_percentage:.2f}%")
print(f"{everest_percentage:.2f}%")