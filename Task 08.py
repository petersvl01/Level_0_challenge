#Task 0.8

def convert_to_preferred_format(num):
    hour = num//60
    minute = num%60
    return(hour, "hours", minute, "minute")

print(convert_to_preferred_format(83))

print(convert_to_preferred_format(145))
