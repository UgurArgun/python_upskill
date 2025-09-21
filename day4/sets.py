elements = {0}
print(type(elements))

elements.add(10)
elements.add(10)
elements.add(20)
elements.add(30)

print(elements)

elements.remove(10)
print(elements)

elements.pop()
print(elements)

elements.update([1, 2, 3])
print(elements)

print("-----------------------------------------------------")


s1 = {"Selenium", "Java", "Python"}
s2 = {"Java", "JavaScript", "Python"}
s3=s1.difference(s2)
print(s3)

print("-----------------------------------------------------")
s4 = s1.intersection(s2)
print(s4)


