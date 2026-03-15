student1 = {"name": "Dana", "age": 22}

student1.clear()

print(student1)

student2 = {"name": "Dana", "age": 22}

student3 = student2.copy()

student2.clear()

print(student3)

keys = ["name", "age", "city"]

person = dict.fromkeys(keys, "unknown")

print(person)

student2 = {"name": "Dana", "age": 22, "address": "Tel Aviv"}
print(student2)
new_student = dict.fromkeys(student2.keys(), "TBD")
print(new_student)

student = {"name": "Dana", "age": 22}

print(student.get("name"))
print(student.get("grade", 'not found'))
# print(student["grade"]) # ERROR

student = {"name": "Dana", "age": 22}

age_value = student.pop("age")

print(age_value)
print(student)
student['age'] = None

student = {"name": "Dana"}

student.setdefault("age", 20)

print(student)

student.setdefault("age", 30)
# student['age'] = 30

print(student)

student = {"name": "Dana"}

student.update({"age": 22, "city": "Paris"})


print({"age": 22,"city": "Paris","num": 22, "num": 23})
'''
  {'age', 'city', 'num'}
  [22, "Paris", 22]
'''

print(student)

student = {"name": "Dana", "age": 22}

print(len(student))

student = {"name": "Dana", "age": 22}

del student["age"]

print(student)