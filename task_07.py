def convert_celsius_to_fahrenheit(c):
    celsius = c
    fahrenheit = (celsius * 1.8) + 32
    return "%.2f celsius = %.2f fahrenheit" %( celsius, fahrenheit)

print(convert_celsius_to_fahrenheit(13))

def convert_fahrenheit_to_celsius(f):
    fahrenheit = f
    celsius = (fahrenheit - 32) * 0.556
    return "%.2f fahrenheit = %.2f celsius" %( fahrenheit, celsius)

print(convert_fahrenheit_to_celsius(50))
