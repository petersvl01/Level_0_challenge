def covert_to_fahrenheit(x):
    celsius = x
    fahrenheit = (celsius * 1.8) + 32
    return "%.2f celsius = %.2f fahrenheit" %( celsius, fahrenheit)

print(covert_to_fahrenheit(13))

def covert_to_celsius(y):
    fahrenheit = y
    celsius = (fahrenheit - 32) * 0.556
    return "%.2f fahrenheit = %.2f celsius" %( fahrenheit, celsius)

print(covert_to_celsius(50))
