#Task 0.8

def convert_to_time(num):
    hour1 = num//60
    minute = num%60
    if hour1 == 1 and minute == 1:
        print(hour1, "hour", minute, "minute")
    elif hour1 > 1 and minute == 1:
        print(hour1, "hours", minute, "minute")
    elif hour1 == 1 and minute > 1:
        print(hour1, "hour", minute, "minutes")
    elif hour1 > 1 and minute > 1:
        print(hour1, "hours", minute, "minutes")
    elif hour1 < 1 and minute > 1:
        print(minute, "minutes")
    elif hour1 == 1 and minute < 1:
        print(hour1, "hour")
    elif hour1 > 1 and minute < 1:
        print(hour1, "hours")
        

convert_to_time(40)
convert_to_time(60)
convert_to_time(120)
convert_to_time(100)
convert_to_time(181)
convert_to_time(310)
