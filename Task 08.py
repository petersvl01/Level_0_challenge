def convert_to_time(num):
    minutes_1 = num % 60
    hour_1 = num // 60
    if hour_1 == 1:
        hour =" hour"
    else:
        hour =" hours"
    if minutes_1 == 1:
        minute =" minute"
    else:
        minute =" minutes"
    print(f'{hour_1} {hour}, {minutes_1} {minute}')
      
convert_to_time(40)
convert_to_time(60)
convert_to_time(310)
