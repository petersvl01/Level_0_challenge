#Task 0.8

def covert_to_time(num):
    hour1 = num//60
    minute = num%60
    if hour1 > 1 and minute > 0:
        print(hour1, "hours", minute, "minutes")
    else:
        print(hour1, "hour", minute, "minutes")

covert_to_time(100)
covert_to_time(310)

