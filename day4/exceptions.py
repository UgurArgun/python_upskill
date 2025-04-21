try:
    x = 100/ 1
    print("This will not be printed")
except ZeroDivisionError as e:
    print("Error: ", e)
    print("You cannot divide by zero")
else:
    print("This will be printed if no exception occurs")
finally:
    print("This will always be printed")
    print("End of the try-except block")

print(("test is completed"))

print("------------------------------------------------")

try :
    raise IndexError()

except ArithmeticError:
    print("Arithmetic error")
except OSError:
    print("OS error")
except Exception as e:
    print("General exception: ", e)

print("------------------------------------------------")

raise Exception("Program is terminated")