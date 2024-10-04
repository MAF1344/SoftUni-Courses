records = float(input())
distance = float(input())
time_per_meter = float(input())

total_distance_time = distance * time_per_meter
resistance_time = (distance // 15) * 12.5
total_time = total_distance_time + resistance_time

if records > total_time:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
else:
    print(f"No, he failed! He was {total_time - records:.2f} seconds slower.")
