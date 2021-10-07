#Task 0.6

def max_num():
    num1 = int(input("enter number: "))
    num2 = int(input("enter number: "))
    num3 = int(input("enter number: "))
    print("max is ", end =" ")
    if num2 <= num1 >= num3:
        print(num1)
    elif num1 <= num2 >= num3:
        print(num2)
    elif num1 <= num3 >= num2:
        print(num3)

print(max_num())