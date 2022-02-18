def area_of_triangle(a, b, c):
    semiperimeter = ((a + b + c) / 2)
    area = ( semiperimeter*( semiperimeter - a) * ( semiperimeter - b) * ( semiperimeter - c))**0.5
    print(area)

area_of_triangle(6, 4, 3)
