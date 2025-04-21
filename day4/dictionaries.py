
student1 = {
    'name': 'John Doe',
    'age': 20,
    'major': 'Computer Science',
    'courses': ['Data Structures', 'Algorithms', 'Database Systems'],
    'grades': {
        'Data Structures': 85,
        'Algorithms': 90,
        'Database Systems': 88
    }
}

student1['name'] = 'Jack London Doe'
student1['name'] = 'Jane Doe'
student1['age'] = 21
student1['grades']['Data Structures'] = 95

student1['departments'] = ['Computer Science', 'Mathematics']

print(student1)

student1.pop('departments')

print(student1)

#student1.popitem()
#print(student1)

print(student1['grades'])


print("-----------------------------------------------------")

employee1 = {
    "employee_name": "Bahadir",
    "employee_id": "A123",
    "job_title": "QA",
    "salary": 100000,
    "skills": ["Python", "Selenium", "Java"],
    "full_time": True
}

for each_key in employee1.keys():
#    print(each_key)
#    print((employees1[each_key]))
    print(f'{each_key} ===> {employee1[each_key]}')

print("-----------------------------------------------------")
for each_pair in employee1.items():
    #print(each_pair)
    print(f"{each_pair[0]} ===> {each_pair[1]}")

print("-----------------------------------------------------")

employee2 = {
    "employee_name": "Ali",
    "employee_id": "A124",
    "job_title": "Dev",
    "salary": 120000,
    "skills": ["Python", "Java", "JavaScript"],
    "full_time": False
}
employee3= {
    "employee_name": "Ayse",
    "employee_id": "A125",
    "job_title": "BA",
    "salary": 110000,
    "skills": ["Python", "SQL", "Java"],
    "full_time": True
}

employees =[employee1, employee2, employee3]
for each_employee in employees:
    print(each_employee)
    print("-----------------------------------------------------")
    for each_pair in each_employee.items():
        print(f"{each_pair[0]} ===> {each_pair[1]}")
"""
for each_dict in employees:
    for each_key in each_dict.keys():
        print(f"{each_key} ===> {each_dict[each_key]}")
    print("-----------------------------------------------------")

"""