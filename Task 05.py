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