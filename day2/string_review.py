n = "Automation testing"

print(n[0])
print(n[-1])


print(len(n))

n = n.lower()
print(n)

print("--------------------------------------")

s = "Python programming Language"
print(s[0:6]) # Python
print(s[7:18]) # programming
print(s[19:26]) # Language
print(s[7:]) # programming Language
print(s[:6]) # Python

reversed_str = s[::-1]
print(reversed_str) # egaugnal gnimmargorp nohtyP

expected_title = "cydeo"
actual_title = "CYDEO"

print(expected_title.lower() == actual_title.lower()) # True
 