
browsers = ("Chrome", "Firefox", "Safari", "Edge", "Internet Explorer")
print(browsers)
print(type(browsers)) # <class 'tuple'>

print(browsers[0]) # Chrome
print(browsers[-1]) # Internet Explorer
print(browsers[-2]) # Edge

print(browsers[0:3]) # ('Chrome', 'Firefox', 'Safari')

a1 = browsers[1:-1]
print(a1) # ('Firefox', 'Safari', 'Edge')

a2 = browsers[2:]
print(a2) # ('Safari', 'Edge', 'Internet Explorer')

a3 = browsers[:-2]
print(a3) # ('Chrome', 'Firefox', 'Safari')

reversed_tuple = browsers[::-1]
print(reversed_tuple) # ('Internet Explorer', 'Edge', 'Safari', 'Firefox', 'Chrome')

result = tuple(reversed(browsers))
print(result) # ('Internet Explorer', 'Edge', 'Safari', 'Firefox', 'Chrome')

print("------------------------------------------------")

for each in browsers:
    print(each)

print("------------------------------------------------")

group_scores = ( (70, 65, 80), (55, 85, 70), (68, 78, 48) )

for i in group_scores:
    #print(i)
    for j in i:
        print(j)

t1 = (1, 2, 3, 4, 5)
t2 = (6, 7, 8, 9, 10, 11, 12)
t3 = (13, 14, 15, 16)

merged_tuples = t1 + t2 + t3
print(merged_tuples) # (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16)