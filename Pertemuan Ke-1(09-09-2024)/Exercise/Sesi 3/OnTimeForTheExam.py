# Input data
exam_hour = int(input())
exam_minute = int(input())
arrival_hour = int(input())
arrival_minute = int(input())

exam_time_in_minutes = exam_hour * 60 + exam_minute
arrival_time_in_minutes = arrival_hour * 60 + arrival_minute

time_difference = arrival_time_in_minutes - exam_time_in_minutes

if time_difference > 0:
    print("Late")
    if time_difference < 60:
        print(f"{time_difference} minutes after the start")
    else:
        hours_late = time_difference // 60
        minutes_late = time_difference % 60
        print(f"{hours_late}:{minutes_late:02d} hours after the start")
elif -30 <= time_difference <= 0:
    print("On Time")
    if time_difference < 0:
        print(f"{-time_difference} minutes before the start")
else:
    print("Early")
    time_difference = abs(time_difference)
    if time_difference < 60:
        print(f"{time_difference} minutes before the start")
    else:
        hours_early = time_difference // 60
        minutes_early = time_difference % 60
        print(f"{hours_early}:{minutes_early:02d} hours before the start")