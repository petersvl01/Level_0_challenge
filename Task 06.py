#Task 0.6

def find_maxno():
    m = [90,78,34]
    higest_number = 0
    for number in m:
        if higest_number < number: 
            higest_number = number
            print(number)
            
print(find_maxno())

def find_maxno():
    m = [90,78,34,100]
    higest_number = 91
    for number in m:
        if higest_number < number: 
            higest_number = number
            print(number)
            
print(find_maxno())