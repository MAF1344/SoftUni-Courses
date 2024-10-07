from collections import deque
from datetime import datetime, timedelta

def convert_to_time(time_str):
    return datetime.strptime(time_str, "%H:%M:%S")

def format_time(time):
    return time.strftime("%H:%M:%S")

robots_input = input().split(";")
robots = []
start_time = convert_to_time(input())

for robot_data in robots_input:
    name, process_time = robot_data.split("-")
    robots.append({
        "name": name,
        "process_time": int(process_time),
        "available_at": start_time
    })

products = deque()
while True:
    product = input()
    if product == "End":
        break
    products.append(product)

current_time = start_time
while products:
    current_time += timedelta(seconds=1)
    product = products.popleft()

    assigned = False
    for robot in robots:
        if robot["available_at"] <= current_time:  # Compare datetime objects
            robot["available_at"] = current_time + timedelta(seconds=robot["process_time"])
            print(f"{robot['name']} - {product} [{format_time(current_time)}]")
            assigned = True
            break

    if not assigned:
        products.append(product)