def convert_to_fahrenheit(x):
    celsius = x
    fahrenheit = (celsius * 1.8) + 32
    print("%.2f celsius = %.2f fahrenheit" %( celsius, fahrenheit))

convert_to_fahrenheit(13)

def convert_to_celsius(y):
    fahrenheit = y
    celsius = (fahrenheit - 32) * 0.556
    print("%.2f fahrenheit = %.2f celsius" %( fahrenheit, celsius))

convert_to_celsius(50)
