import csv
visitors=[]
num=int(input("Enter the number of visitors:: "))
for i in range(num):
        name=input("Enter name of visitors:: ")
        address=input("Enter address of visitors:: ")
        contact=int(input("Enter contact number of visitors::"))
        visitors.append([name,address,contact])
with open('visitors1.csv','w') as file:
    writer=csv.writer(file)
    writer.writerow(['Name','Address','Contact'])
    writer.writerows(visitors)

