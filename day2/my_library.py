import numbers


def addition(num1:numbers, num2:numbers, num3:numbers=0, num4:numbers=0) -> numbers:
    return num1 + num2 +num3 + int(num4)

def cube(num: numbers) -> numbers:
    return num ** 3

def square(num: numbers) -> numbers:
    return num ** 2