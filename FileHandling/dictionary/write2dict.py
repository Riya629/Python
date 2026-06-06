import csv
num=int(input("Enter the number of visitors:: "))
students=[]
for i in range(num):
    name=input("Enter name:: ")
    address=input("Enter address:: ")
    contact=int(input("Enter contact::"))
    students.append({
        'name':name,
        'address':address,
        'contact':contact
        })
with open('students7.csv','w', newline='') as file:
    writer=csv.DictWriter(file, fieldnames=['name','address','contact'])
    writer.writeheader()
    writer.writerows(students)


