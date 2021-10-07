#Task 0.5

def area_of_triangle():
    a = int(input("enter the length of first side: "))
    b = int(input("enter the length of first side: "))
    c = int(input("enter the length of first side: "))
    s = ((a + b + c)/2)
    area = (s*(s-a) * (s-b) * (s-c))**0.5
    print(s)
    print(area)
    
area_of_triangle()
