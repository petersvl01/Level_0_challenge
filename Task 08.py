#Task 0.8

def convert_to_time(num):
    minutes1 = num % 60
    hour1 = num // 60
    if hour1 == 1:
        hour=" hour"
    else:
        hour=" hours"
    if minutes1 == 1:
        minute=" minute"
    else:
        minute=" minutes"
    print(hour1, hour,",", minutes1, minute)
      

convert_to_time(100)
convert_to_time(181)
convert_to_time(310)
