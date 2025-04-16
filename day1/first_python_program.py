print('Python Programming')

# This is a comment

"""
This is a multi-line comment
"""

name_of_student = "Elena"
print(name_of_student)
print(type(name_of_student))

name_of_student = 3.5
print(name_of_student)
print(type(name_of_student))


name_of_student= True
print(name_of_student)
print(type(name_of_student))

s ='35'

num = int(s)
print(num)
print(type(num))

print("------------------------------------------------")

prog_language = "Python"
version = 3.13

print("My programming language is {} and version is {}".format(prog_language, version))
print(f"My programming language is {prog_language} and version is {version}")


str1 = "python programming"
print ("python" in str1) # True

print (True and True)
print (True and False)
print (False and True)
print (False or True)

print("------------------------------------------------")

score = int( input("Please enter your score: \n") )
while score < 0 or score > 100:
    print("Invalid score. Please enter a score between 0 and 100.")
    score = int( input("Please enter your score: \n") )
if 0 <= score <= 100:
    if score >= 60:
        print("You have passed the exam")
    else:
        print("You have failed the exam")
