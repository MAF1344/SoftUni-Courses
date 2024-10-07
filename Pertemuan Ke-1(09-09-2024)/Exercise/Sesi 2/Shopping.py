budget = float(input())
video_card = int(input())
video_card_price = video_card * 250
CPU = int(input())
CPU_price = video_card_price * (35/100) * CPU
RAM = int(input())
RAM_price = video_card_price * (10/100) * RAM

bill = video_card_price + CPU_price + RAM_price

if video_card > CPU:
    bill = bill - (bill * 15/100)

if budget >= bill:
    print(f"You have {budget - bill:.2f} USD left!")
else:
    print(f"Not enough money! You need {bill - budget:.2f} USD more!")
