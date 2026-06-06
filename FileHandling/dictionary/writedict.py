import csv
student={
    'name':'Riya',
    'age':20,
    'address':'Bharatpur-12'
}
with open('student6.csv','w',newline='') as file:
    writer=csv.DictWriter(file,fieldnames=student.keys())
    writer.writeheader()
    writer.writerow(student)
    
