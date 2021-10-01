#Task 1

x = 0
y = 1

print(x)
print(y)

x = x + 3
y = y + x

print(x)
print(y)

#Task 0.2

x = 1 + 1 * 2
y = (1 + 1) * 2
z = 1 + ( 1 * 2 )
a = 1 + 1 * 2 / 2
b = (1 + 1 * 2 ) / 2

print(x)
print(y)
print(z)
print(a)
print(b)


#Task 0.3
def hello_func(hello):
    return "Hello {} !".format(hello)

print(hello_func("Tshepo"))

#Task 0.4

def even_or_odd(input):
    if input % 3 == 0:
        return "Odd"
    if input % 4 == 0:
        return "Even"
    return input

print(even_or_odd(3))

print(even_or_odd(4))

#Task 0.5

b = 6
h = 4
a = 0.5

print(b)
print(h)
print(a)

print(a * (b*h))

def area_of_triangle(a, b, h):
    return (a + b) == h or (b + h) >= a and (a+h) <= b 

print(area_of_triangle(0.5, 0.5, 0.5))
print(area_of_triangle(0.5, 0.5, 6))
print(area_of_triangle(0.5, 6, 4))


#Task 0.6

a = (2,4,6)
print(a)

print(a[0])

print(a[len(a) - 1])

maximum=(2, 4, 6)
def max_num(max):
    return max % 1 == 0 and max % 3 != 0 or max % 22 == 0

print(max_num(2))

#Task 0.7

Celsius = 4
Fahrenheit = (Celsius * 1.8) + 32

print("%.2f Celsius = %.2f Fahrenheit" %( Celsius, Fahrenheit))

Celsius = 5/9 *(Fahrenheit -32)

def Fahrenheit_to_Celsius(Fahrenheit):
    return Celsius 

print(Fahrenheit_to_Celsius(Fahrenheit))


#Task 0.8





#Task 0.9
#Task 0.10



