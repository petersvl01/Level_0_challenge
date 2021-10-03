#Task 0.4

def even_or_odd(input):
    if input % 3 == 0:
        return "Odd"
    if input % 4 == 0:
        return "Even"
    return input

print(even_or_odd(3))

print(even_or_odd(4))