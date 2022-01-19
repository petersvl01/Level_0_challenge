#Task 0.7

def covert_to_Fahrenheit(x):
    Celsius = x
    Fahrenheit = (Celsius * 1.8) + 32
    print("%.2f Celsius = %.2f Fahrenheit" %( Celsius, Fahrenheit))

covert_to_Fahrenheit(13)

def covert_to_Celsius(y):
    Fahrenheit = y
    Celsius = (Fahrenheit - 32) * 0.556
    print("%.2f Fahrenheit = %.2f Celsius" %( Fahrenheit, Celsius))

covert_to_Celsius(50)
