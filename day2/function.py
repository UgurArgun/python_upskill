import numbers


def return_value():
    return 1000

print(return_value())

def return_integer() -> int:
    print("This is int function")

return_integer()

def cube(num: int) -> int:
    return num ** 3

print(cube(3)) # 27

def addition(num1:numbers, num2:numbers, num3:numbers=0, num4:numbers=0) -> numbers:
    return num1 + num2 +num3 + int(num4)

print(addition(3, 5.5)) # 8.5
print(addition(3, 5, 11)) # 19
print(addition(3, 5, 11, "400")) # 419


