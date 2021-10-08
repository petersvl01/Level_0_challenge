#Task 0.5

def area_of_triangle():
    a = 10
    b = 20
    c = 20
    s = ((a + b + c)/2)
    area = (s*(s-a) * (s-b) * (s-c))**0.5
    print(area)
    
area_of_triangle()
