import math

series_name = input()
episode_duration = int(input())
break_duration = int(input())

lunch_time = break_duration / 4
rest_time = break_duration / 8
time_left = break_duration - lunch_time - rest_time

if time_left >= episode_duration:
    time_spare = time_left - episode_duration
    print(f"You have enough time to watch {series_name} and left with {math.ceil(time_spare)} minutes free time.")
else:
    time_needed = episode_duration - time_left
    print(f"You don't have enough time to watch {series_name}, you need {math.ceil(time_needed)} more minutes.")