ModelName = "GPT-4"
Temperature = "0.7"
Maximum_tokens = "1000"
api_version = "V1"

print("Model Configuration Values")
print("Model Name:" , ModelName)
print("Temperature:" , Temperature)
print("Maximum Tokens:" , Maximum_tokens)
print("Api Version :" , api_version)

student = {
            "Name" : "kinjal",
            "Course" : "PGDCA",
            "Semester" : "1",
            "Marks" : "70"
}


print("\nstudent Details")
for key,value in student.items():
     print(key,":",value)

print("\nupdate student Details")
new_marks = int(input("Enter a Marks"))
if new_marks >=0 and new_marks<=100:
     student["Marks"] = new_marks
     
    
else:
     print("\nInvalid Marks")

print("\nUpdate dictionary")
for key,value in student.items():
     print(key ,":", value)

import os 
file_name = input("\nEnter the file name")

if os.path.exists(file_name):

     size = os.path.getsize(file_name)
     print("File Name : ", file_name)
     print("File size:",size,"bytes")
     if size ==0:
          print("File is Empty.")
     else:
          print("File is Not Empty.")
else:
     print(f"\n This file {file_name} dose not exist.")
