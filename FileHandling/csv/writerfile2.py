
import csv
num=int(input("Enter the number of students to records:"))
with open('student5.csv','w',newline='') as file:
    writer=csv.writer(file)
    writer.writerow(['Name','Age','Address'])
    for i in range(num):
        name=input("Enter name")
        age=int(input("Enter age"))
        address=input("Enter address")
        writer.writerow([name,age,address])