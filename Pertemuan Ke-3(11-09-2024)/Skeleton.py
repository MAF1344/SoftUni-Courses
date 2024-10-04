minutes = int(input())
seconds = int(input())
length = float(input())
meter100 = float(input())

control_time = (minutes * 60) + seconds
time_decrease = (length / 120) * 2.5
malcolm_time = (length / 100) * meter100 - time_decrease

if malcolm_time <= control_time:
    print("Malcolm Davidson won an Olympic quota!")
    print(f"His time is {malcolm_time:.3f}.")
else:
    needed_seconds = malcolm_time - control_time
    print(f"No, Malcolm failed! He was {needed_seconds:.3f} second slower.")