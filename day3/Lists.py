items = ["apple", "banana", "cherry"]
print(items[0])  # apple
print(type(items))  # <class 'list'>
print(len(items))

items.append("strawberry")
print(items)  # ['apple', 'banana', 'cherry', 'strawberry']
items.insert(1, "orange")
print(items)  # ['apple', 'orange', 'banana', 'cherry', 'strawberry']
items.remove("banana")
print(items)  # ['apple', 'orange', 'cherry', 'strawberry']
items.pop(2)
print(items)  # ['apple', 'orange', 'strawberry']
items.clear()
print(items)  # []

items.extend( ( ("apple", "orange", "banana"), ("cherry", "strawberry") ) )

print(items)  # [('apple', 'orange', 'banana'), ('cherry', 'strawberry')]
items[0] = "kiwi"

languages = ("Java", "Python", "JavaScript", "C++", "Ruby")

temp_list = list(languages)
temp_list.pop(1)
temp_list.append("PHP")
temp_list.remove("JavaScript")

languages =tuple(temp_list)
print(languages)

print("------------------------------------------------------")

nums = []
for x in range(1,31):
    nums.append(x)

print(nums)

divisible_by_three = [p for p in nums if p % 3 == 0]
print(divisible_by_three)




