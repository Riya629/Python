import csv
file=open('student3.csv','a', newline='')
writer=csv.writer(file)
writer.writerow(['Name','Age','Address'])
writer.writerow(['Riya',20,'Munalchowk'])
writer.writerow(['sachet',25,'Gitanagar'])
file.close()