day = input()
switch_day = {
    'Monday': 'Working day',
    'Tuesday': 'Working day',
    'Wednesday': 'Working day',
    'Thursday': 'Working day',
    'Friday': 'Working day',
    'Saturday': 'Weekend',
    'Sunday': 'Weekend',
}
print(switch_day.get(day, "Error"))