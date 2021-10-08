#Task 0.7

def covert_to_Fahrenheit():
    Celsius = 13
    Fahrenheit = (Celsius * 1.8) + 32
    print("%.2f Celsius = %.2f Fahrenheit" %( Celsius, Fahrenheit))

covert_to_Fahrenheit()

def covert_to_Celsius():
    Fahrenheit = 50
    Celsius = (Fahrenheit - 32) * 0.556
    print("%.2f Fahrenheit = %.2f Celsius" %( Fahrenheit, Celsius))

covert_to_Celsius()