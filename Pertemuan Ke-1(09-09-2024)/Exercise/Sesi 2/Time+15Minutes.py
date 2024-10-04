hour = int(input())
minute = int(input())
addMinute = minute + 15
minuteLeft = addMinute % 60

if addMinute >= 60:
    hour += 1

if hour >= 24:
    hour -= 24

if minuteLeft < 10:
    print(f"{hour}:0{minuteLeft}")
else:
    print(f"{hour}:{minuteLeft}")



