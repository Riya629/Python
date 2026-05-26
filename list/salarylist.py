employee=[]
for i in range(3):
    name=input("enter name:")
    age=int(input("Enter age:"))
    address=input("Enter address:")
    employee.append([name])
    employee.append([age])
    employee.append([address])
print(employee)
for emp in employee:
    print(f"{emp}")

