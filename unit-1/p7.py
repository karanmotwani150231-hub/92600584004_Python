student={
        "name":"karan",
        "age":21,
        "course":"BCA",
        "marks":85
        }

print("original dictionary :")
print(student)

print("\n name :",student["name"])
print("\n marks :",student["marks"])

print("\nkeys :",student.keys())
print("\nitems :",student.items())
print("\nvalues :",student.values())

student["city"]="Rajkot"
print("\n aftr adding city :",student)

student["marks"]=90
print("\n aftr updating marks :",student)

student.pop("age")
print("\n after removing age :",student)

print("\nIs 'course' present? ","course" in student)
print("\n dictonary keys :")
for key in student :
    print(key)

print("\n dictonary values :")
for value in student.value() :
    print(value)

print("\n dictonary items :")
for key, value in student.items() :
    print(key, ":",value)    
