import json

Students = []

N = int(input("Enter the number of student:"))

for i in range(N):
    print("Enter details for student" ,{i+1})
    name = input("Student Name:")
    age = input("Age")
    course = input("Course")
    Student = {  
                     "Name" : name,
                     "Age"  : age,
                     "course" : course 
                  }
    Students.append(Student)

with open("student.json","w") as file:
    json.dump(Students,file,indent=5)
print("Data stored successfully.")

with open("student.json","r") as file:
     data = json.load(file)

print("student Records")


for student in data:
    print("Name:",student["Name"])
    print("Age:" , student["Age"])
    print("Course:",student["course"])
    print()