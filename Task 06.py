#Task 0.6

def find_max(x, y, z):
    if x >= y and x >= z:
        return x
    elif y >= x and y >= z:
        return y
    elif z >= x and z >= y:
        return z
    else:
        return "Match"

print(find_max(50,20,35))


def find_max(x, y, z, num):
    if x >= y and x <= z:
        return x
    elif y >= x and y >= z:
        return y
    elif z >= x and z <= y:
        return z
    else:
        return num

print(find_max(50,20,35,60))
