# Students=[]
# for i in range(3):
#     name=input("Enter name:")
#     address=input("Enter address:")
#     salary=float(input("Enter salaray:"))
#     Students.append([name, address,salary])
# print("Students details:")
# for students in Students:
#     print(f"Name:{students[0]}\t address:{students[1]} \tsalary:{students[2]}\t")




















Students=[]
num=int(input("Enter number of student:"))
for i in range(num):
    name=input("Enter name:")
    age=int(input("Enter age:"))
    Students.append({
        "name":name,
        "age":age
    })
print("Students details----")
for students in Students:
    print(f"Name:{students['name']}\n Age:{students['age']}")